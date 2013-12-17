# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

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
