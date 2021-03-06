from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('content.views',
    # Examples:
    # url(r'^$', 'newspaper.views.home', name='home'),
    # url(r'^newspaper/', include('newspaper.foo.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    url(r'^article/(?P<article_id>\d+)/$', 'get_article'),
    url(r'^$', 'home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
