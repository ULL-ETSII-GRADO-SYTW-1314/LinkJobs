from django.conf.urls.defaults import patterns,url
from django.conf import settings

urlpatterns=patterns('perfil.views',
	url(r'^(?P<username>\w+)/$', 'user_details',name='vista_perfil'),
	url (r'^(?P<username>\w+)/imagen/$','subirimagen',name='vista_subirImagen'),
	url (r'^(?P<username>\w+)/curriculum/(?P<completado>\w+)/$','subircurriculum',name='vista_curriculum'),
	url (r'^(?P<username>\w+)/ver_curriculum/$','view_curriculum',name='vista_curriculum'),
	url (r'^(?P<username>\w+)/perfil/(?P<id>\w+)$','ver_perfil',name='vista_perfil'),
	url (r'^(?P<username>\w+)/noticias/$','home_noticias',name='vista_noticias'),
	url (r'^(?P<username>\w+)/curriculum/(?P<id>\w+)$','ver_su_curriculum',name='vista_de_curriculum'),
	url (r'^(?P<username>\w+)/seguir/(?P<id>\w+)$','seguir',name='vista_seguir'),
	url (r'^(?P<username>\w+)/sigues_a/$','quien_sigues',name='vista_quien_sigues'),
	url (r'^borrar/(?P<id>\w+)/$','borrar_post',name='vista_borrarpost'),
	url (r'^(?P<username>\w+)/no_seguir/(?P<id>\w+)$','noseguir',name='vista_de_noseguir'),
	url (r'^(?P<username>\w+)/te_siguen/$','quien_te_sigue',name='vista_quien_te_sigue'),
)


