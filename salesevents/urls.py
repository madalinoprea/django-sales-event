from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^logout', 'catalog.views.logout_view', name='logout'),
    url(r'^', include('catalog.urls')),

    url(r'^signuprequest', 'catalog.views.signup_view', name='signup_request'),
    (r'^accounts/', include('registration.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

# Allow dev server to deliver media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
