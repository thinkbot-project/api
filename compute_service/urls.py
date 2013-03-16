from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compute_service.views.home', name='home'),
    # url(r'^compute_service/', include('compute_service.foo.urls')),

    url(r'^', include('snippets.urls')),
    url(r'^', include('jobs.urls')),

    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
)
