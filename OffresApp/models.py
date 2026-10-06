from django.db import models

from EntreprisesApp.models import Entreprise
from ExpeditionsApp.models import Expedition
from VehiculesApp.models import Vehicule
from django.core.exceptions import ValidationError
# Create your models here.
class Offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    delai_jours = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('en_attente','En attente'),('acceptee','Acceptée'),('refusee','Refusée')], default='en_attente')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    date_proposition = models.DateField()
    expedition = models.ForeignKey(Expedition, on_delete=models.CASCADE, related_name='offres')
    entreprise =models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='offres')
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, related_name='offres')
    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'trans':
            raise ValidationError({"entreprise": "L'entreprise associée doit être de type 'transporteur' pour créer une offre."})
        if self.vehicule_id and self.vehicule.proprietaire_id != self.entreprise_id:
            raise ValidationError({"vehicule": "Le véhicule proposé doit appartenir à l'entreprise associée à l'offre."})
        