from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
admin.site.site_header = 'Columbia COI Administration'

urlpatterns = patterns('',
	# Admin
	url(r'^admin/', include(admin.site.urls)),
	
	# Link to app_coi/urls.py
	url(r'', include('app_coi.urls')),
) \
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)	  \
