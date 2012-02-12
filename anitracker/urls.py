from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('anitracker.views',
    url('^$', 'index', name='index')
)

urlpatterns += staticfiles_urlpatterns()
