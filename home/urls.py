from django.conf.urls.defaults import *


urlpatterns = patterns('home.views',
    url (r'^$','home_view',name='vista_home'),
    url (r'^about/$','about_view',name='vista_about'),
    url (r'^privacity/$','privacity_view',name='vista_privacidad'),
    url (r'^terms_of_use/$','terms_of_use_view',name='vista_terminos'),
    url (r'^contact/$','contact_view',name='vista_contacto'),
    url (r'^faq/$','faq_view',name='vista_faq'),
    url (r'^help/$','help_view',name='vista_ayuda'),

    url(r'^logout/$', 'logout',name='vista_logout'),
    url (r'^signup/$','signup_view',name='vista_signup'),
    url (r'^login/$','login_view',name='vista_login'),
)