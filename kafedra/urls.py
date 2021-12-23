# -*-coding:utf8-*-

from django.conf.urls import patterns, include, url
from kafedra.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home),
    url(r'^directions/pmi/$', directions),
    url(r'^events/conferences/$', events, {'event': 'conf', 'year': False}),
    url(r'^events/publications/$', events, {'event': 'publ', 'year': False}),
    url(r'^events/publications/(?P<year>\w{4})/$', events, {'event': 'publ'}),
    url(r'^studentam/raspisanie/$', studentam, {'studentam': 'rasp'}),
    url(r'^studentam/kursovye/$', studentam, {'studentam': 'kurs'}),
    url(r'^studentam/diplomnye/$', studentam, {'studentam': 'dipl'}),
    url(r'^laboratories/innovations/$', laboratories, {'laboratory': 'innov'}),
    url(r'^laboratories/cisco/$', laboratories, {'laboratory': 'cisco'}),
    url(r'^contacts/$', contacts),
    url(r'^about/collective/$', collective),
    url(r'^about/news/$', news, {'news_id': False}),
    url(r'^about/news/(\d+)/$', news),
    url(r'^about/info/$', info),
    url(r'^sitemap/$', sitemap),
    url(r'^search/$', search),
    url(r'^vypuskniki/gallery/$', gallery),
    # url(r'^kafedra/', include('kafedra.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
