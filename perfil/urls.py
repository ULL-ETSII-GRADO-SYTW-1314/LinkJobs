
from django.conf.urls.defaults import patterns,url
from django.conf import settings

urlpatterns=patterns('perfil.views',
	url (r'^/perfil/$','profile_view',name='vista_perfil'),
)


