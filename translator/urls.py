from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^translate', views.translate, name='post'),
  url(r'^retrieve', views.getTranslations),
]