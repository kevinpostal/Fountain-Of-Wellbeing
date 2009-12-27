from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^fwb/', include('fwb.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
     
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/media' % settings.PROJECT_PATH }),
     
    (r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/medias' % settings.PROJECT_PATH }),
        
    # Contact Page Urls 
    (r'^contact/', include('contact_form.urls')),
    
    # Menu Pages Urls
    (r'^menu/', 'budadex.views.menu_view'),
    
    # Home Redirect
    (r'^$', 'django.views.generic.simple.redirect_to', {'url':'/home'})


) 

urlpatterns += patterns('django.contrib.flatpages.views',
   (r'^(?P<url>.*)$', 'flatpage'),
)


