from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from budadex.models import Strain
from django.template import RequestContext

# Create your views here.



def menu_view(request):
    
    #set up the dictonary
    context = {}
    
    
    #Define Storage dictonary for active menu

    context['strain'] = Strain.objects.filter(active=True).values()
    
    return render_to_response('menu.html',context,context_instance=RequestContext(request))