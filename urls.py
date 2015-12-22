from django.contrib import admin
from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt  

from .scrapping.parser import ParseUrls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^([a-zA-Z]+)/parse$', csrf_exempt(ParseUrls.as_view())),
]

