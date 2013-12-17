from django.conf.urls.defaults import *

urlpatterns=patterns('perfil.views',
	url (r'^profile/$','profile_view',name='vista_perfil'),
)


