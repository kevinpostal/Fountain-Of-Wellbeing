from django.contrib import admin
from flatcontent.models import FlatContent
from django.db import models

class FlatContentAdmin(admin.ModelAdmin):
    list_display = ('slug',)
    ordering = ('slug',)

admin.site.register(FlatContent, FlatContentAdmin)

