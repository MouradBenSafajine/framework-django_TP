"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from magasin.views import login1,register,home,logout1,majproduits,nouveauFournisseur,index,vetrine




urlpatterns = [    path('',index,name='index'),

        path ('vetrine/', vetrine,name='vetrine'),

    path('magasin/', include('magasin.urls')),
    path ('majProduits/', majproduits,name='nproduit'),
    path('nouveauFournisseur/', nouveauFournisseur, name='nouveauFour'),

path('admin/', admin.site.urls),
 path('api-auth/', include('rest_framework.urls')),

path('signup/',register,name='register'),

path('login/',login1,name='login'),
path('logout/',logout1,name='logout'),
path('home/',home,name='home'),



]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
