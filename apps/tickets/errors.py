# -*- coding: utf-8 -*-
#
from django.utils.translation import ugettext_lazy as _

from common.exceptions import JMSException


class AlreadyClosed(JMSException):
    default_detail = _("Ticket already closed")
