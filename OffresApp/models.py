from django.db import models

from EntreprisesApp.models import Entreprise
from ExpeditionsApp.models import Expedition
from VehiculesApp.models import Vehicule
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
class Offre(models.Model):
    prix = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.01, "Le prix doit être supérieur à zéro")])
    delai_jours = models.IntegerField(validators=[MinValueValidator(1, "Le délai doit être d'au moins 1 jour")])
    statut = models.CharField(max_length=20, choices=[('proposee','Proposée'),('acceptee','Acceptée'),('refusee','Refusée')], default='proposee')
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
        if self.pk is None and self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError({"expedition": "L'expédition associée doit être de statut 'publiee' pour créer une offre."})
        if self.statut == 'proposee' and Offre.objects.filter(expedition_id=self.expedition_id, entreprise_id=self.entreprise_id, statut='proposee').exclude(pk=self.pk).exists():
            raise ValidationError({"entreprise": "Cette entreprise a déjà une offre proposée sur cette expédition."})
        if self.pk is None and self.vehicule_id and not self.vehicule.disponible:
            raise ValidationError({"vehicule": "Le véhicule proposé n'est pas disponible pour créer une offre."})
        if self.vehicule_id and self.expedition_id:
            poids = self.expedition.poids_kg
            type_vehicule = self.vehicule.type_vehicule
            if type_vehicule == 'camionnette' and poids > 1500:
                raise ValidationError({"vehicule": "Une camionnette transporte jusqu'à 1500 kg."})
            if type_vehicule == 'fourgon' and poids > 3500:
                raise ValidationError({"vehicule": "Un fourgon transporte jusqu'à 3500 kg."})
            if type_vehicule == 'camion_porteur' and (poids < 3500 or poids > 19000):
                raise ValidationError({"vehicule": "Un camion porteur transporte entre 3500 et 19000 kg."})
            if type_vehicule == 'semi_remorque' and (poids < 19000 or poids > 26000):
                raise ValidationError({"vehicule": "Une semi-remorque transporte entre 19000 et 26000 kg."})

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        if self.statut == 'acceptee':
            self.expedition.statut = 'attribuee'
            self.expedition.save()
            Offre.objects.filter(expedition_id=self.expedition_id, statut='proposee').update(statut='refusee')
