from django.conf.urls import patterns, include, url

import lists.views as views

urlpatterns = [
    url(r'^(\d+)/$',
        views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$',
        views.add_item, name='add_item'),
    url(r'^new$',
        views.new_list, name='new_list'),
]
