from django.conf.urls.defaults import patterns, include, url
from catalog.views import home, event, product

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^event/(?P<event_id>\d+)', event, name='event'),
#    url(r'^event/(?P<event_id>\d+)/sort/(?P<sort_by>\w+)/(?P<dir>\w+)', 'catalog.views.event', name='event_sortby'),
    url(r'^p/(?P<product_id>\d+)', product, name='product'),
    # url(r'^', include('catalog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
