from django.core.exceptions import ValidationError
from django.db import models

from EntreprisesApp.models import Entreprise
from django.core.validators import MinValueValidator
class Vehicule(models.Model):
    CAPACITE_MAX_KG = {'camionnette': 1500, 'fourgon': 3500, 'camion_porteur': 19000, 'semi_remorque': 26000}
    immatriculation = models.CharField(max_length=11, unique=True)
    type_vehicule = models.CharField(choices=[('camionnette','Camionnette / utilitaire léger'),('camion_porteur','Camion porteur'),('semi_remorque','Semi-remorque'),('fourgon','Fourgon')], max_length=20,default='camionnette')
    capacite_kg = models.IntegerField(validators=[MinValueValidator(100,"La capacité doit être d'au moins 100 kg")])
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    proprietaire = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='vehicules')
    def clean(self):
        super().clean()
        if self.proprietaire_id and self.proprietaire.type_entreprise != 'trans':
             raise ValidationError({"proprietaire": "L'entreprise associée doit être de type 'transporteur' pour créer un véhicule."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
