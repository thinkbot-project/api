from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf import settings

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

from . import views


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.HomePageView.as_view(), name="home"),
    url(r'^about/$', views.AboutPageView.as_view(), name="about"),
    url(r'^docs/$', views.DocsPageView.as_view(), name="docs"),
    url(r'^pricing/$', views.PricingPageView.as_view(), name="pricing"),
    url(r'^support/$', views.SupportPageView.as_view(), name="support"),
    url(r'^legal/$', views.LegalPageView.as_view(), name="legal"),
    url(r'^dashboard/$', views.DashboardPageView.as_view(), name="dashboard"),

    url(r'^activate/complete/$', TemplateView.as_view(template_name='registration/activation_complete.html'), name='registration_activation_complete'),
    url(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
    url(r'^signup/$', RegistrationView.as_view(), name='registration_register'),
    url(r'^signup/complete/$', TemplateView.as_view(template_name='registration/registration_complete.html'), name='registration_complete'),
    url(r'^signup/closed/$', TemplateView.as_view(template_name='registration/registration_closed.html'), name='registration_disallowed'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    (r'', include('registration.auth_urls')),

    url(r'^api/v1/', include('jobs.urls')),
    url(r'^backend/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^results/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
