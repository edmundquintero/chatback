from django.conf.urls import patterns, include, url
from chatback.views import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Index),
    url(r'^admin/', include(admin.site.urls)),
    # -- API routs
    url(r'^room/(?P<pk>\d+)/$', RoomDetail.as_view(), name='room-detail'),
    url(r'^room/$', RoomList.as_view(), name='room-list'),
)
