from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.books.views import home_view, autocomplete


urlpatterns = patterns(
    '',

    url(r'^$', home_view, name='home'),
    url(r'^autocomplete/(?P<query>[\w|\W]+)/$', autocomplete, name='autocomplete'),
    url(r'^admin/', include(admin.site.urls)),
)
