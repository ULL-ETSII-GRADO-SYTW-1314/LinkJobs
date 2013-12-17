# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def profile_view(request):
	return render_to_response('perfil/perfil.html',context_instance=RequestContext(request))