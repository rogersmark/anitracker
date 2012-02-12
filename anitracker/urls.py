from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('anitracker.views',
    url('^$', 'index', name='index'),
    url('^species/specie\.json',
        'specie_type_json', name='specie-type-json'
    ),
)

urlpatterns += staticfiles_urlpatterns()
