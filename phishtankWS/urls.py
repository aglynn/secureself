from django.conf.urls import patterns, url
from phishtankWS import views

urlpatterns = patterns('',
                       url(r'^$', views.ipCheck, name='ipCheck'),
)