from django.db import models
from Gestion.settings import AUTH_USER_MODEL
# Create your models here.


class Revenue(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = [("salaire", "salaire"),
                  ("Business", "Business")]
    name = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_AJOUT = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    categorie = models.CharField(max_length=100, choices=categories)
    
    def get_total(self):
        return Revenue.objects.aaggregate(sum('montant'))['montant__sum']
    
    def __str__(self):
        return self.user.username

    
class Depense(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    categories = [("loyer", "loyer"),
                  ("manger", "manger"), 
                  ("transport", "transport"),
                  ("devertissement", "divertisssemnt")]
    name = models.CharField(max_length=100)
    montant = models.IntegerField()
    date_AJOUT = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    categorie = models.CharField(max_length=100, choices=categories)
    
    def get_total(self):
        total = Depense.objects.filter(user=self.user).aggregate(total=sum('montant'))['total']
        return total or 0
    
    def __str__(self):
        return self.user.username