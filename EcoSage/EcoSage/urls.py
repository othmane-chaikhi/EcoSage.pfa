"""
URL configuration for EcoSage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from EcoSageApp import urls as EcoSageApp_urls
from login import urls as  login_urls
from firstPage import urls as  firstPage_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',include(EcoSageApp_urls)),#the home page EcoSage
    path('login/',include(login_urls)),#the  log in and register pages 
     path('',include(firstPage_urls)),#the  firstpage in and register pages 
]
