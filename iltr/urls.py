from django.conf.urls import patterns, include, url
from django.contrib import admin

from apps.books.views import home_view, book_or_author


urlpatterns = patterns(
    '',

    url(r'^$', home_view, name='home'),
    url(r'^book_or_author/(?P<query>[\w|\W]+)/$', book_or_author, name='book_or_author'),
    url(r'^admin/', include(admin.site.urls)),
)
