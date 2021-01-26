# re_path: constroi rotas usando regex
from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<nome_sala>[^/]+)/$', ChatConsumer.as_asgi()),
    # re_path(r"ws/chat/(?P<nome_sala>\W+)/$", ChatConsumer.as_asgi()),
]