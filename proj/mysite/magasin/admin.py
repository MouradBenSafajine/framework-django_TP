from django.contrib import admin
from django.db import models


# Register your models here.

from django.contrib import admin
from .models import Produit
from .models import categorie
from .models import Fournisseur
from .models import ProduitC
from .models import ProduitNC
from .models import Commande
admin.site.register(Produit)
admin.site.register(categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitC)
admin.site.register(ProduitNC)
admin.site.register(Commande)





