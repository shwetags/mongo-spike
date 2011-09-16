from django.conf.urls.defaults import patterns, include, url
from views import create, show, home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
#    (r'^project/questionnaire/(?P<project_id>.+?)/$', questionnaire),
    url(r'^create/(?P<name>.+?)/$', create),
    url(r'^show/$', show),
    url(r'^home/$', home),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),

    # Examples:
    # url(r'^$', 'mongo_auth.views.home', name='home'),
    # url(r'^mongo_auth/', include('mongo_auth.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
