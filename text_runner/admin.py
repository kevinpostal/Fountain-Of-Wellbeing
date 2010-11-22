from django.contrib import admin
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from text_runner.models import Patient, Text_Log
from django.http import HttpResponseRedirect
from django.db.models import F
from googlevoice import Voice
from settings_local import *

class Text_LogAdmin(admin.ModelAdmin):
    list_display = ['patient', 'number_texted','message','creation_date']
    list_filter = ('patient', 'number_texted')
    search_fields = ['user__email']
    ordering = ['creation_date']
    date_hierarchy = 'creation_date'


class AddMsgForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    message = forms.CharField(widget=forms.Textarea)
    #tag = forms.ModelChoiceField(Patient.objects)
    
class TextAdmin(admin.ModelAdmin):
    actions = ['Text_Selected','Text_All']
    
    def Text_All(self,request, queryset):
        context = {}
        if 'apply' in request.POST:
            form = AddMsgForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data['message']
                voice = Voice()
                voice.login(GVOICE_EMAIL,GVOICE_PASS)

                for user in queryset:
                    textlog = Text_Log(patient=user,number_texted=user.phone_number,message=message)
                    voice.send_sms(user.phone_number, message)
                    Patient.objects.filter(id=user.id).update(msg_amount = F('msg_amount')+1)
                    textlog.save()
                    return HttpResponseRedirect(request.get_full_path())
        
        context['users'] = Patient.objects.all()
        context['form'] =  AddMsgForm()

        return render_to_response('admin/Text_Selected.html',context,context_instance=RequestContext(request))
    Text_All.short_description = "Text All Users"
    
    def Text_Selected(self,request, queryset):
        context = {}
        if 'apply' in request.POST:
            form = AddMsgForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data['message']
                voice = Voice()
                voice.login(GVOICE_EMAIL,GVOICE_PASS)

                for user in queryset:
                    textlog = Text_Log(patient=user,number_texted=user.phone_number,message=message)
                    voice.send_sms(user.phone_number, message)
                    Patient.objects.filter(id=user.id).update(msg_amount = F('msg_amount')+1)
                    textlog.save()
                    return HttpResponseRedirect(request.get_full_path())

        selected = request.POST.getlist(admin.ACTION_CHECKBOX_NAME)
        context['form'] =  AddMsgForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        context['users'] = Patient.objects.filter(id__in=selected)

        return render_to_response('admin/Text_Selected.html',context,context_instance=RequestContext(request))
    Text_Selected.short_description = "Text Selected Users"

admin.site.register(Text_Log)
admin.site.register(Patient,TextAdmin)