# ~*~ coding: utf-8 ~*~

import json
import os
import re
import time
from urllib.parse import urlparse, quote

import pytz
from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.http.response import HttpResponseForbidden
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils import timezone

from .utils import set_current_request


class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.META.get('HTTP_X_TZ')
        if not tzname or tzname == 'undefined':
            return self.get_response(request)
        try:
            tz = pytz.timezone(tzname)
            timezone.activate(tz)
        except pytz.UnknownTimeZoneError:
            pass
        response = self.get_response(request)
        return response


class DemoMiddleware:
    DEMO_MODE_ENABLED = os.environ.get("DEMO_MODE", "") in ("1", "ok", "True")
    SAFE_URL_PATTERN = re.compile(
        r'^/users/login|'
        r'^/api/terminal/v1/.*|'
        r'^/api/terminal/.*|'
        r'^/api/users/v1/auth/|'
        r'^/api/users/v1/profile/'
    )
    SAFE_METHOD = ("GET", "HEAD")

    def __init__(self, get_response):
        self.get_response = get_response

        if self.DEMO_MODE_ENABLED:
            print("Demo mode enabled, reject unsafe method and url")
            raise MiddlewareNotUsed

    def __call__(self, request):
        if self.DEMO_MODE_ENABLED and request.method not in self.SAFE_METHOD \
                and not self.SAFE_URL_PATTERN.match(request.path):
            return HttpResponse("Demo mode, only safe request accepted", status=403)
        else:
            response = self.get_response(request)
            return response


class RequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        set_current_request(request)
        response = self.get_response(request)
        return response


class RefererCheckMiddleware:
    def __init__(self, get_response):
        if not settings.REFERER_CHECK_ENABLED:
            raise MiddlewareNotUsed
        self.get_response = get_response
        self.http_pattern = re.compile('https?://')

    def check_referer(self, request):
        referer = request.META.get('HTTP_REFERER', '')
        referer = self.http_pattern.sub('', referer)
        if not referer:
            return True
        remote_host = request.get_host()
        return referer.startswith(remote_host)

    def __call__(self, request):
        match = self.check_referer(request)
        if not match:
            return HttpResponseForbidden('CSRF CHECK ERROR')
        response = self.get_response(request)
        return response


class SQLCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        if not settings.DEBUG_DEV:
            raise MiddlewareNotUsed

    def __call__(self, request):
        from django.db import connection
        response = self.get_response(request)
        response['X-JMS-SQL-COUNT'] = len(connection.queries) - 2
        return response


class StartMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        if not settings.DEBUG_DEV:
            raise MiddlewareNotUsed

    def __call__(self, request):
        request._s_time_start = time.time()
        response = self.get_response(request)
        request._s_time_end = time.time()
        if request.path == '/api/health/':
            data = response.data
            data['pre_middleware_time'] = request._e_time_start - request._s_time_start
            data['api_time'] = request._e_time_end - request._e_time_start
            data['post_middleware_time'] = request._s_time_end - request._e_time_end
            response.content = json.dumps(data)
            response.headers['Content-Length'] = str(len(response.content))
            return response
        return response


class EndMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        if not settings.DEBUG_DEV:
            raise MiddlewareNotUsed

    def __call__(self, request):
        request._e_time_start = time.time()
        response = self.get_response(request)
        request._e_time_end = time.time()
        return response


class SafeRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not (300 <= response.status_code < 400):
            return response
        if request.resolver_match and request.resolver_match.namespace.startswith('authentication'):
            # 认证相关的路由跳过验证（core/auth/xxxx
            return response
        location = response.get('Location')
        if not location:
            return response
        parsed = urlparse(location)
        if parsed.scheme and parsed.netloc:
            target_host = parsed.netloc
            if target_host in [*settings.ALLOWED_HOSTS]:
                return response
            origin = f"{request.scheme}://{request.get_host()}"
            target_origin = f"{parsed.scheme}://{target_host}"
            if not target_origin.startswith(origin):
                safe_redirect_url = '%s?%s' % (reverse('redirect-confirm'), f'next={quote(location)}')
                return redirect(safe_redirect_url)
        return response
