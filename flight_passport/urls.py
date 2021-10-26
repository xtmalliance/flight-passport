"""flight_passport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from vault import views as vault_views
from django.views.generic import TemplateView
import django.views.defaults as default_views

from dotenv import load_dotenv, find_dotenv
import os
from django.conf import settings as settings

from django.conf.urls import (handler400, handler403, handler404, handler500)

# handler404 = vault_views.NotFoundView.as_view()
# handler500 = vault_views.ErrorView.get_rendered_view()

urlpatterns  = []
if settings.SHOW_ADMIN: 
    admin.site.site_header = 'Flight Passport Administration'
    admin.site.site_title = 'Flight Passport Administration'
    urlpatterns += [path('admin/', admin.site.urls)]


urlpatterns += [
    
    path("oauth/", include('oauth2_provider.urls', namespace='oauth2_provider')),    
    # path("oauth/", include('oauth2_provider_jwt.urls', namespace='oauth2_provider_jwt')),
    path("accounts/email/", default_views.page_not_found, kwargs={"exception": Exception("Page not Found")},),   
    
    path("accounts/", include('allauth.urls')),
    
    path('', vault_views.HomePage.as_view(), name='home'),
]
