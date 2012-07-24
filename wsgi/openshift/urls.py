from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^$','openshift.views.home'),                       
    (r'^register/$', 'openshift.views.EstudianteRegistration'),
    (r'^login/$','openshift.views.LoginRequest'),
    (r'^logout/$','openshift.views.LogoutRequest'),
    (r'^profile/$','openshift.views.profile'),
)
