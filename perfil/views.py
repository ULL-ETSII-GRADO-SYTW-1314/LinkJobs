from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from perfil.forms import FormMicropost
from home.forms import UserForm, ImagenForm, CompleteForm
from django.template import RequestContext
from django.core.urlresolvers import reverse
from home.models import User, Follow, Micropost
from datetime import datetime


def quien_te_sigue(request, username):
        if antesdeLogin(request):
                valido = False;
                completado = False;
                FormularioImagen = ImagenForm(request.POST, request.FILES)
                user = get_object_or_404 (User,username=request.session['username'])
                if user.curriculum == "":
                        completado = True
                allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]

                id_te_siguen = Follow.objects.filter(follow = user.id).values_list('user', flat=True)
                siguen = User.objects.filter(id__in=id_te_siguen)
                
                if request.method == 'POST':
                        if FormularioImagen.is_valid():
                                photo = FormularioImagen.cleaned_data['photo']
                                user.InsertarFoto(photo)
                                user.save()
                                ctx = {'siguen': siguen, 'completado':completado,'user':user, 'allUser': allUser, 'FormularioImagen': FormularioImagen, 'valido': valido}
                                return render (request,'perfil/tesiguen.html',ctx)
                else:
                        FormularioImagen = ImagenForm()
                ctx = {'siguen':siguen, 'completado':completado,'valido': valido, 'allUser':allUser, 'user':user, 'FormularioImagen':FormularioImagen}
                return render (request,'perfil/tesiguen.html',ctx)
        else:
                HttpResponseRedirect(reverse('home.views.home_view'))

def borrar_post (request, id):
	if antesdeLogin(request):
		Micropost.objects.filter(id=id).delete()
		return HttpResponseRedirect(reverse('post.views.user_details',args=[request.session['username']]))
	else:
		return HttpResponseRedirect(reverse('home.views.login'))

def noseguir (request, username, id):
        if antesdeLogin(request):
                user = get_object_or_404 (User,username=request.session['username'])
                sigue_a = get_object_or_404 (User,id=id)
                Follower = Follow();
                Comprobar = Follow.objects.filter(user_id=user.id).filter(follow_id=id)
                Comprobar.delete()
                return HttpResponseRedirect(reverse('perfil.views.quien_sigues',args=[request.session['username']]))
        else:
                HttpResponseRedirect(reverse('home.views.home_view')) 


def quien_sigues (request, username):
	if antesdeLogin(request):
		post = ""
		valido = False;
		completado = False;
		FormularioImagen = ImagenForm(request.POST, request.FILES)
		user = get_object_or_404 (User,username=request.session['username'])
		if user.curriculum == "":
			completado = True
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]

		id_seguidores = Follow.objects.filter(user = user.id).values_list('follow', flat=True)
		seguidores = User.objects.filter(id__in=id_seguidores)
		
		if request.method == 'POST':
			if FormularioImagen.is_valid():
				photo = FormularioImagen.cleaned_data['photo']
				user.InsertarFoto(photo)
				user.save()
				ctx = {'seguidores': seguidores, 'completado':completado,'user':user, 'allUser': allUser, 'FormularioImagen': FormularioImagen, 'valido': valido}
				return render (request,'perfil/sigues.html',ctx)
		else:
			FormularioImagen = ImagenForm()
		ctx = {'seguidores':seguidores, 'completado':completado,'valido': valido, 'allUser':allUser, 'user':user, 'FormularioImagen':FormularioImagen}
		return render (request,'perfil/sigues.html',ctx)
	else:
		HttpResponseRedirect(reverse('home.views.home_view'))


def seguir (request, username, id):
	if antesdeLogin(request):
		user = get_object_or_404 (User,username=request.session['username'])
		sigue_a = get_object_or_404 (User,id=id)
		Follower = Follow();
		Comprobar = Follow.objects.filter(user_id=user.id).filter(follow_id=id)
		if len(Comprobar) == 0:
			Follower.InsertarSeguidor(user, sigue_a)
			Follower.save()

		return HttpResponseRedirect(reverse('perfil.views.quien_sigues',args=[request.session['username']]))
	else:
		HttpResponseRedirect(reverse('home.views.home_view'))	



def home_noticias(request, username):
	if antesdeLogin(request):
		post = ""
		valido = False;
		completado = False;
		FormularioImagen = ImagenForm(request.POST, request.FILES)
		user = get_object_or_404 (User,username=request.session['username'])

		id_seguidores = Follow.objects.filter(user = user.id).values_list('follow', flat=True)
		all_micropost = Micropost.objects.filter(user_id__in=id_seguidores)


		if user.curriculum == "":
			completado = True
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]
		if request.method == 'POST':
			if FormularioImagen.is_valid():
				photo = FormularioImagen.cleaned_data['photo']
				user.InsertarFoto(photo)
				user.save()
				ctx = {'all_micropost':all_micropost,'completado':completado,'user':user, 'allUser': allUser, 'FormularioImagen': FormularioImagen, 'valido': valido}
				return render (request,'perfil/noticias.html',ctx)
		else:
			FormularioImagen = ImagenForm()
		ctx = {'all_micropost':all_micropost,'completado':completado,'valido': valido, 'allUser':allUser, 'user':user, 'FormularioImagen':FormularioImagen}
		return render (request,'perfil/noticias.html',ctx)
	else:
		HttpResponseRedirect(reverse('home.views.home_view'))


def ver_perfil(request,username, id):
	if antesdeLogin(request):
		user = get_object_or_404 (User,id=id)
		user_sug = get_object_or_404 (User, username= request.session['username'])
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]
		Mostrar = Micropost.objects.filter(user=user.id).order_by('date')

		comprobacion = Follow.objects.filter(user=user_sug.id).filter(follow=id)

		if not comprobacion:
			return HttpResponse("No puedes acceder aqui")
		else:	
			ctx = {'user_sug':user_sug,'allUser':allUser,'user':user, 'Mostrar': Mostrar}
			return render (request,'perfil/perfil.html',ctx)

	else:
		return HttpResponseRedirect(reverse('home.views.login'))


def view_curriculum(request, username):
	if antesdeLogin(request):
		post = ""
		valido = False;
		completado = False;
		FormularioImagen = ImagenForm(request.POST, request.FILES)
		user = get_object_or_404 (User,username=request.session['username'])
		if user.curriculum == "":
			completado = True
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]
		if request.method == 'POST':
			if FormularioImagen.is_valid():
				photo = FormularioImagen.cleaned_data['photo']
				user.InsertarFoto(photo)
				user.save()
				ctx = {'completado':completado,'user':user, 'allUser': allUser, 'FormularioImagen': FormularioImagen, 'valido': valido}
				return render (request,'perfil/ver_curriculum.html',ctx)
		else:
			FormularioImagen = ImagenForm()
		ctx = {'completado':completado,'valido': valido, 'allUser':allUser, 'user':user, 'FormularioImagen':FormularioImagen}
		return render (request,'perfil/ver_curriculum.html',ctx)
	else:
		HttpResponseRedirect(reverse('home.views.home_view'))


def subircurriculum(request,username, completado):
	if antesdeLogin(request):
		valido = False
		completado = False;
		FormularioImagen = ImagenForm(request.POST, request.FILES)
		FCurriculum = CompleteForm(request.POST)
		user = get_object_or_404 (User,username=request.session['username'])
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]
		if request.method == "POST":
			if FCurriculum.is_valid():
				curriculum = FCurriculum.cleaned_data['curriculum']
				profesion = FCurriculum.cleaned_data['profesion']
				user.InsertarCurriculum(curriculum, profesion)
				user.save()
				completado = True
				return HttpResponseRedirect(reverse('perfil.views.user_details',args=[request.session['username']]))
		else:
			MicroPost = FormMicropost()
			FormularioImagen = ImagenForm()
			FCurriculum = CompleteForm()
		ctx = {'valido': valido, 'allUser':allUser, 'user':user, 'FormularioImagen':FormularioImagen,'FCurriculum':FCurriculum}
		return render (request,'perfil/curriculum.html',ctx)
	else:
		return HttpResponseRedirect(reverse('home.views.login'))






def ver_su_curriculum(request, username, id):
	if antesdeLogin(request):
		user = get_object_or_404 (User,id=id)
		user_sug = get_object_or_404 (User, username= request.session['username'])
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]

		comprobacion = Follow.objects.filter(user=user_sug.id).filter(follow=id)

		if not comprobacion:
			return HttpResponse("No puedes acceder aqui")
		else:
			ctx = {'user_sug':user_sug, 'user':user, 'allUser': allUser}
			return render (request,'perfil/su_curriculum.html',ctx)
	else:
		HttpResponseRedirect(reverse('home.views.home_view'))




def subirimagen(request, username):
	if antesdeLogin(request):
		post = ""
		valido = True;
		completado = False;
		MicroPost = FormMicropost(request.POST)
		FormularioImagen = ImagenForm(request.POST, request.FILES)
		user = get_object_or_404 (User,username=request.session['username'])
		if user.curriculum == "":
			completado = True
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]
		if request.method == 'POST':
			if FormularioImagen.is_valid():
				photo = FormularioImagen.cleaned_data['photo']
				user.InsertarFoto(photo)
				user.save()
				ctx = {'completado':completado,'MicroPost':MicroPost,'user':user, 'allUser': allUser, 'FormularioImagen': FormularioImagen, 'valido': valido}
				return render (request,'perfil/valid.html',ctx)
			if MicroPost.is_valid():
				m = Micropost()
				post = MicroPost.cleaned_data['post']
				today = datetime.now()
				m.insertar(user,post,today)
				m.save()
				Mostrar = Micropost.objects.filter(user=user.id).order_by('date')
		else:
			MicroPost = FormMicropost()
			FormularioImagen = ImagenForm()
		Mostrar = Micropost.objects.filter(user=user.id).order_by('date')
		ctx = {'completado':completado, 'valido': valido, 'allUser':allUser,'MicroPost':MicroPost, 'user':user, 'FormularioImagen':FormularioImagen, 'Mostrar': Mostrar}
		return render (request,'perfil/valid.html',ctx)
	else:
		HttpResponseRedirect(reverse('home.views.home_view'))



def antesdeLogin(request):
	if 'username' in request.session:
		return True
	else:
		return False

def user_details(request,username):
	if antesdeLogin(request):
		valido = False
		completado = False
		post = ""
		MicroPost = FormMicropost(request.POST)
		FormularioImagen = ImagenForm(request.POST, request.FILES)
		user = get_object_or_404 (User,username=request.session['username'])
		if user.curriculum == "":
			completado = True
		allUser = User.objects.order_by('?').exclude(username=request.session['username'])[:4]
		if request.method == "POST":
			if MicroPost.is_valid():
				m = Micropost()
				post = MicroPost.cleaned_data['post']
				today = datetime.now()
				m.insertar(user,post,today)
				m.save()
				id_post = Micropost.objects.filter(user = user.id).values_list('post', flat=True)
				Mostrar = User.objects.filter(id__in=id_post)
				Mostrar = Micropost.objects.filter(user=user.id).order_by('id')
				print Mostrar
				ctx = {'completado': completado, 'valido': valido, 'allUser':allUser, 'MicroPost':MicroPost, 'user':user, 'Mostrar': Mostrar}
				return render (request,'perfil/valid.html',ctx)
		else:
			MicroPost = FormMicropost()
			FormularioImagen = ImagenForm()
		Mostrar = Micropost.objects.filter(user=user.id).order_by('date')
		ctx = {'completado': completado, 'valido': valido, 'allUser':allUser,'MicroPost':MicroPost, 'user':user, 'FormularioImagen':FormularioImagen, 'Mostrar': Mostrar}
		return render (request,'perfil/valid.html',ctx)
	else:
		return HttpResponseRedirect(reverse('home.views.login'))
