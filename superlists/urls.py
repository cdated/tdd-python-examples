from django.conf.urls import patterns, include, url
from django.contrib import admin

import lists.views as views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/(\d+)/$',
        views.view_list, name='view_list'),
    url(r'^lists/(\d+)/add_item$',
        views.add_item, name='add_item'),
    url(r'^lists/new$',
        views.new_list, name='new_list'),
    # url(r'^admin/', include(admin.site.urls))
]
