from django.urls import path, re_path

from .views import IndexView, SalaView

app_name = 'chat'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    re_path(r'^(?P<nome_sala>[^/]+)/$', SalaView.as_view(), name='sala'),
    # path('<str:nome_sala>/', SalaView.as_view(), name='sala'),
]