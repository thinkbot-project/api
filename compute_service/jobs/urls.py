from django.conf.urls import include, patterns, url

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# API endpoints
urlpatterns = format_suffix_patterns(patterns('jobs.views',
    url(r'^$', 'api_root'),
    url(r'^jobs/$',
        views.JobList.as_view(),
        name='job-list'),
    url(r'^jobs/(?P<pk>[0-9]+)/$',
        views.JobDetail.as_view(),
        name='job-detail'),
    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail')
))

# Login and logout views for the browsable API
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token'),
)
