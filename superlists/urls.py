from django.conf.urls import patterns, include, url
from django.contrib import admin

import lists.views as views

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/', include('lists.urls'))
    # url(r'^admin/', include(admin.site.urls))
]
