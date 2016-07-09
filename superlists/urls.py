from django.conf.urls import patterns, include, url
from django.contrib import admin

from lists.views import home_page
from lists.views import view_list

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^lists/the-only-list-in-the-world/$',
        view_list, name='view_list'),
    url(r'^admin/', include(admin.site.urls))
]
