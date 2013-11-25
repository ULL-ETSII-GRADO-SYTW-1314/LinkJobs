from django.conf.urls.defaults import *


urlpatterns = patterns('home.views',
    url(r'^$','home_view',name='vista_home'),
    url(r'^about/$','about_view',name='vista_about'),
    url(r'^privacidad/$','privacidad_view',name='vista_priva'),
    url(r'^terminos/$','terminos_view',name='vista_terminos'),

    url (r'^signup/$','signup',name='vista_signup'),
)