from django.urls import path

from .. import ws

app_name = 'common'

urlpatterns = [
    path('ws/setting/tools/', ws.ToolsWebsocket.as_asgi(), name='setting-tools-ws'),
]
