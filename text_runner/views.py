from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from text_runner.models import Patient

import csv
def send_text(request,user_ids):

    #set up the dictonary
    context = {}
    list = user_ids.split(',')

    context['test'] = list
    context['users'] = Patient.objects.filter(id__in=user_ids)
    
    return render_to_response('admin/text_patients.html',context,context_instance=RequestContext(request))
