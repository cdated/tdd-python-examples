from django.conf.urls import patterns, include, url
from django.contrib import admin

from lists.views import home_page

urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^admin/', include(admin.site.urls))
]
