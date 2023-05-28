from django.shortcuts import render
from django.template import loader
from .models import Fournisseur, Produit
from .forms import FournisseurForm
from .forms import ProduitForm
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import categorie
from magasin.forms import CategorySerializer


from django.contrib.auth import login, authenticate,logout

from django. contrib.auth.models import User


@login_required
def index(request):
   return render(request,'magasin/base.html')

def majproduits(request):
 if request.method == "POST" : 
   form = ProduitForm(request.POST,request.FILES)
   if form.is_valid():
    form.save()
   return HttpResponseRedirect('/magasin')
 else :
   form = ProduitForm() #créer formulaire vide
   return render(request,'magasin/majProduits.html',{'form':form})

def vetrine(request):
   produits=Produit.objects.all()
   return render(request,'magasin/vitrine.html',{'produits':produits})

def nouveauFournisseur(request):
    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin')
    else:
        form = FournisseurForm()
    return render(request, 'magasin/fournisseur.html', {'form': form})



def fournisseurs(request):
    list = Fournisseur.objects.all()
    return render(request, 'magasin/fournisseur.html', {'list': list})

def home(request):
    return render(request,'magasin/home.html')

def register(request):   
    if request.method=='POST':
       user=request.POST.get("username")
       email=request.POST.get("email")
       passw=request.POST.get("password")
       c_password=request.POST.get("confirm_password")
       if passw!=c_password:
          return HttpResponse("incorrect password confirm !!")
       m_user=User.objects.create_user(user,email,passw)
       m_user.save()
       return redirect('login')

    return render(request,'magasin/registration/register.html')
def login1(request):
   if request.method=='POST':
       user=request.POST.get("username")
       password1=request.POST.get("password")
       usern=authenticate(request,username=user,password=password1)
       print(user,password1)

       if usern is not None:
         
         login(request,usern)
         return redirect(index)
       else:
         return redirect('login')
         

   
   return render(request,'magasin/registration/login.html')

def logout1(request):
    logout(request)
    return redirect(login1)





class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
     categories = categorie.objects.all()
     serializer = CategorySerializer(categories, many=True)
     return Response(serializer.data)




