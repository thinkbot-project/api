from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

from . import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url(r'^about/$', views.AboutPageView.as_view(), name="about"),
    url(r'^docs/$', views.DocsPageView.as_view(), name="docs"),
    url(r'^help/$', views.SupportPageView.as_view(), name="support"),
    url(r'^terms/$', views.LegalPageView.as_view(), name="legal"),

    url(r'^api/v1/', include('jobs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^results/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
