from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.hello.views import PersonDetail

urlpatterns = patterns('',
    url(r'^(?P<pk>[0-9]+)/$', PersonDetail.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
