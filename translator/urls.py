from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^translate', views.translate),
  url(r'^retrieve', views.retrieve),
]