from django.conf.urls.defaults import *


urlpatterns = patterns('home.views',
    url(r'^$','home_view',name='vista_home'),
    url(r'^about/$','about_view',name='vista_about'),
    url(r'^privacity/$','privacity_view',name='vista_priva'),
    url(r'^terms_of_use/$','terms_of_use_view',name='vista_terminos'),

    url (r'^signup/$','signup',name='vista_signup'),
    url (r'^login/$','login',name='vista_login'),
)