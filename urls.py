from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    (r'^grappelli/', include('grappelli.urls')),     
        
    # Contact Page Urls 
    (r'^contact/', include('contact_form.urls')),
    
    # Menu Pages Urls
    (r'^menu/', 'budadex.views.menu_view'),

    #Admin
    (r'^admin/(.*)', admin.site.root),

    #Text_Runner
    (r'^text/(?P<user_ids>.*)/$', 'text_runner.views.send_text',),

    # Home Redirect
    (r'^$', 'django.views.generic.simple.redirect_to', {'url':'/home'})


) 

urlpatterns += patterns('django.contrib.flatpages.views',
   (r'^(?P<url>.*)$', 'flatpage'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s' % "/var/virtualenvs/fwb/app/grappelli/media/" }),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '%s/static' % settings.PROJECT_PATH }),
        )
    