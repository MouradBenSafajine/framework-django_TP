from django.db import models
from datetime import datetime

class Produit(models.Model):
   TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')] 
   libelle=models.CharField(max_length=100)
   description=models.TextField()
   prix=models.DecimalField(max_digits=10, decimal_places=3)
   type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
   Img=models.ImageField(blank=True)
   categorie=models.ForeignKey("Categorie",on_delete=models.CASCADE,null=True)
   Fournisseur=models.ForeignKey("Fournisseur",on_delete=models.CASCADE,null=True)
   def __str__(self):
    return self.libelle+" "+self.description+" "+str(self.prix)

class categorie(models.Model):
   TYPE_CHOICES=[("Al","Alimentaire"), ("Mb","Meuble"),
        ("Sn","Sanitaire"), ("Vs","Vaisselle"),
        ("Vt","Vêtement"),("Jx","Jouets"),
        ("Lg","Linge de Maison"),("Bj","Bijoux"),("Dc","Décor"),
        ("Im","Immobilier"),("Me","Meuble"),("Pp","ParaPharmacie"),
        ("El","Electroménager"),("Fr","Frais"),("Ta","Tapis"),
        ("CI","Composant Informatique"),
        ("JV","Jeux Video"),
        
        
        
        ]
   type=models.TextField(max_length=50,choices=TYPE_CHOICES,default="Ai")
   
   def __str__(self):
    return self.type
class Fournisseur(models.Model):
    name=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    def __str__(self):
        return "\nNom : "+self.name+"\nAdresse : "+self.adresse+"\nEmail : "+self.email+"\nTelephone : "+str(self.telephone) 
class ProduitNC(Produit) : 
    Duree_garantie=models.CharField(max_length=100)           
     

class ProduitC(Produit) : 
    Duree_garantie=models.CharField(max_length=100)


class Commande(models.Model):
    dateCde=models.DateField(null=True,default=datetime.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    produit=models.ManyToManyField('Produit')
    def __str__(self): 
        return "\n Date Commande : "+(self.dateCde).strftime('%Y-%m-%d')+"\nTotal : "+str(self.totalCde)
