from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from .views import CategoryAPIView

from . import views
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('nouvFournisseur/', views.nouveauFournisseur, name='nouveauFour'),
        path('fournisseurs/', views.fournisseurs, name='fournisseurs'),
         path('api/category/', CategoryAPIView.as_view()),

      


     
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

        




