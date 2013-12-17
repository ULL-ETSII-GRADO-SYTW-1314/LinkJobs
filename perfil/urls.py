from django.conf.urls.defaults import patterns,url
from django.conf import settings

urlpatterns=patterns('perfil.views',
	url(r'^(?P<username>\w+)/$', 'user_details',name='vista_perfil'),
	url (r'^(?P<username>\w+)/imagen/$','subirimagen',name='vista_subirImagen'),
)


