from django.conf.urls import patterns, url

from listing1 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.show, name='show'), 
    #url(r'^(?P<post_id>\d+)/$', views)
)

