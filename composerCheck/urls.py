from django.conf.urls import patterns, url

from composerCheck import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^vulnerability$', views.vulnerability, name='vulnCheck'),
    url(r'^file$', views.check, name='checkFile'),
    url(r'^vulnerability/(?P<vulnerability_id>[^/]+)/$', views.detail, name='detail'),
    url(r'^secureself$', views.secureself, name='secureself'),
)
