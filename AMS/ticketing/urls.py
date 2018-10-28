from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<id>[0-9]+)/ticket/$', views.ticket, name='ticket'),
    url(r'^(?P<id>[0-9]+)/cancel/$', views.cancel, name='cancel'),
    url(r'^(?P<id>[0-9]+)/book/$', views.book, name='book'),
    url(r'^employee/$', views.employee, name='employee'),
    url(r'^flight/$', views.flight, name='flight'),
]
