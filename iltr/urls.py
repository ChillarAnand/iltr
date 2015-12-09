from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.books.views import home, search
from django.conf import settings



urlpatterns = patterns(
    '',

    url(r'^$', home, name='home'),
    url(r'^search', search, name='search'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': settings.MEDIA_ROOT,
                                 }),
                            )
    
