"""
Definition of urls for NYCCC.
"""

from django.conf.urls import include, url
from app.views import home

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = [
    # Examples:
    url(r'^$', home, name='home')
    # url(r'^NYCCC/', include('NYCCC.NYCCC.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
