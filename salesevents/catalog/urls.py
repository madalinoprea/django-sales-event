__author__ = 'madalinoprea'

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'catalog.views.home_view', name='home'),
    url(r'^event/(?P<event_slug>[\w-]+)$', 'catalog.views.event_view', name='event'),
    url(r'^event/(?P<event_slug>[\w-]+)/(?P<category_slug>[\w-]+)$', 'catalog.views.event_category_view', name='event_category'),
    url(r'^event/(?P<event_slug>[\w-]+)/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)$', 'catalog.views.event_product_view', name='event_product'),

#    url(r'^event/(?P<event_id>\d+)/sort/(?P<sort_by>\w+)/(?P<dir>\w+)', 'catalog.views.event', name='event_sortby'),
    url(r'^p/(?P<product_id>\d+)', 'catalog.views.product_view', name='product'),
    url(r'^signuprequest', 'catalog.views.signup_view', name='signup_request'),
)
