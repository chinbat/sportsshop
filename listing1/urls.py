from django.conf.urls import patterns, url

from listing1 import views

urlpatterns = patterns('',
    url(r'^ranking/$', views.ranking,name='ranking'),
    url(r'^shop/$', views.shop,name='shop'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.show, name='show'), 
    url(r'^football/$', views.football,name='football'),
    url(r'^basketball/$', views.basketball,name='basketball'),
)

