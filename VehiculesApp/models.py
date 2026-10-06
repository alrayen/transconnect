from django.db import models

from EntreprisesApp.models import Entreprise
from OffresApp.models import Offre
from django.core.validators import MinValueValidator
# Create your models here.
class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=11, unique=True)
    type_vehicule = models.CharField(choices=[('cam','camionnette'),('four','fourgon'),('camp','camion porteur'),('semi','semi-remorque')], max_length=20,default='cam')
    capacite_kg = models.IntegerField(validators=[MinValueValidator(100,"La capacité doit être d'au moins 100 kg")])
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    proprietaire = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='vehicules')
    offre = models.ForeignKey(Offre, on_delete=models.SET_NULL, null=True, blank=True, related_name='vehicules')