from django.db import models

from EntreprisesApp.models import Entreprise
from django.core.exceptions import ValidationError
# Create your models here.
class Expedition(models.Model):
    reference = models.CharField(max_length=20, unique=True)
    ville_depart = models.CharField(max_length=100)
    ville_arrivee = models.CharField(max_length=100)
    poids_kg = models.DecimalField(max_digits=10, decimal_places=2)
    date_souhaitee = models.DateField()
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=[('en_attente','En attente'),('en_cours','En cours'),('terminee','Terminée')], default='en_attente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='expeditions')
    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'char':
            raise ValidationError({"entreprise": "L'entreprise associée doit être de type 'chargeur' pour créer une expédition."})
            
