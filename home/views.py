from home.models import User
from home.forms import ContactForm,UserForm, LoginForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.shortcuts import redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.mail import EmailMultiAlternatives #para enviar emails HTML

def home_view(request):
	return render_to_response('home/index.html',context_instance=RequestContext(request))

def about_view(request):
  return render_to_response('home/about.html',context_instance=RequestContext(request))

def privacity_view(request):
  return render_to_response('home/privacidad.html',context_instance=RequestContext(request))

def terms_of_use_view(request):
  return render_to_response('home/terminos.html',context_instance=RequestContext(request))

def contact_view(request):
    valido = False
    email = ""
    asunto = ""
    texto = ""
    if request.method == "POST":
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
           valido = True
           email = formulario.cleaned_data['email']
           asunto = formulario.cleaned_data['asunto']
           texto = formulario.cleaned_data['texto']
           #configuracion enviando mensaje via GMAIL
           to_admin = 'linkjobsull@gmail.com' #el password de esta cuenta esta en el google drive 
           html_content = "Informacion recibida <br><br><br>***MENSAJE***<br><br>%s" % (texto)
           msg= EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com', [to_admin])
          # SUBJECT,CONTENT,DESTINATARIO
           msg.attach_alternative(html_content,'text/html') #definimos el contenido como html
           msg.send() #enviamos
           #fin configuracion del servidor GMAIL
           ctx = {'formulario':formulario,'email':email,'asunto':asunto,'texto':texto,'valido':valido}
           return render_to_response ('home/contacto.html',ctx,context_instance=RequestContext(request))
    else:
        formulario = ContactForm()
    ctx = {'formulario':formulario,'email':email,'asunto':asunto,'texto':texto,'valido':valido}
    return render_to_response ('home/contacto.html',ctx,context_instance=RequestContext(request))

def faq_view(request):
  return render_to_response('home/faq.html',context_instance=RequestContext(request))

def help_view(request):
  return render_to_response('home/ayuda.html',context_instance=RequestContext(request))

def signup_view(request):
  password1 = ""
  password2 = ""
  nombre = ""
  apellidos = ""
  username = ""
  email1 = ""
  if request.method == "POST":
    formulario = UserForm(request.POST)
    if formulario.is_valid():
      nombre = formulario.cleaned_data['nombre']
      apellidos = formulario.cleaned_data['apellidos']
      username = formulario.cleaned_data['username']
      email1 = formulario.cleaned_data['email1']
      password1 = formulario.cleaned_data['password1']
      b = User()
      b.insertar (nombre,apellidos,username,email1,password1)
      b.save()

      #configuracion enviando mensaje via GMAIL
      user= '%s'%(email1);
      html_content = "<p>Bienvenido a LinkJobs</p> <p>Tus datos personales son los siguientes:</p><p><b>Nombre:</b> %s</p><p><b>Apellidos:</b> %s</p><p><b>Username:</b> %s</p><p><b>email:</b> %s</p><p><b>Password:</b> %s</p>"%(nombre,apellidos,username,email1,password1)
      msg= EmailMultiAlternatives('Registro exitoso en LinkJobs',html_content,'from@server.com',[user])
      # SUBJECT,CONTENT,DESTINATARIO
      msg.attach_alternative(html_content,'text/html') #definimos el contenido como html
      msg.send() #enviamos

      #fin configuracion del servidor GMAIL

      return HttpResponseRedirect(reverse('home.views.login_view'))
  else:
    formulario = UserForm()
  ctx = {'formulario':formulario}
  return render_to_response ('home/signup.html',ctx,context_instance=RequestContext(request))
  
def login_view (request):
  password = ""
  username = ""
  if request.method == "POST":
      formulario = LoginForm(request.POST)
      if formulario.is_valid():
          m = User.objects.get(username=request.POST['username'])
          username = formulario.cleaned_data['username']
          request.session['username'] = m.username
          return HttpResponseRedirect(reverse('perfil.views.user_details', args=[m.username]))

  else:
      formulario = LoginForm()
  ctx = {'formulario':formulario}
  return render_to_response ('home/login.html', ctx,context_instance=RequestContext(request))


def logout(request):
  try:
    del request.session['username']
  except KeyError:
    pass
  return HttpResponseRedirect(reverse('home.views.home_view'))