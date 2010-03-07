from django.contrib import admin
from budadex.models import Strain




class BudAdmin(admin.ModelAdmin):
    actions = ['make_active','make_inactive']
   
    def make_active(self,request, queryset):
        rows_updated = queryset.update(active=True)
        if rows_updated == 1:
            message_bit = "1 item was"
        else:
            message_bit = "%s items were" % rows_updated
        self.message_user(request, "%s successfully marked as active." % message_bit)
    
    make_active.short_description = "Mark selected as active"

    
    def make_inactive(self,request, queryset):
            rows_updated = queryset.update(active=False)
            if rows_updated == 1:
                message_bit = "1 item was"
            else:
                message_bit = "%s items were" % rows_updated
            self.message_user(request, "%s successfully marked as inactive." % message_bit)
    
    make_inactive.short_description = "Mark selected as inactive"


# admin stuff
    list_display = ( 'name','description', 'thumb_photo','active',)
    list_filter = ('active','last_modified')    

    
    ordering = ['name']

admin.site.register(Strain, BudAdmin)
