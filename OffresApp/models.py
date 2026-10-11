from django.db import models, transaction

from EntreprisesApp.models import Entreprise
from ExpeditionsApp.models import Expedition
from VehiculesApp.models import Vehicule
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone
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
        if self._state.adding and self.expedition_id and self.expedition.statut != 'publiee':
            raise ValidationError({"expedition": "L'expédition associée doit être de statut 'publiee' pour créer une offre."})
        if self.statut == 'proposee' and self.expedition_id and self.entreprise_id:
            doublon = Offre.objects.filter(
                expedition_id=self.expedition_id,
                entreprise_id=self.entreprise_id,
                statut='proposee',
            ).exclude(pk=self.pk).exists()
            if doublon:
                raise ValidationError("Cette entreprise a déjà une offre proposée active sur cette expédition.")
        if self.vehicule_id and not self.vehicule.disponible:
            raise ValidationError({"vehicule": "Le véhicule proposé n'est pas disponible pour créer une offre."})
        if self.vehicule_id and not self.vehicule.disponible:
            raise ValidationError({"vehicule": "Le véhicule proposé n'est pas disponible pour créer une offre."})
        if self.vehicule_id and self.expedition_id:
            max_kg = Vehicule.CAPACITE_MAX_KG.get(self.vehicule.type_vehicule)
            if max_kg is not None and self.expedition.poids_kg > max_kg:
                raise ValidationError({"vehicule": f"Un véhicule de type '{self.vehicule.get_type_vehicule_display()}' ne peut pas transporter {self.expedition.poids_kg} kg (maximum {max_kg} kg)."})

    def save(self, *args, **kwargs):
        self.full_clean()
        with transaction.atomic():
            super().save(*args, **kwargs)
            if self.statut == 'acceptee':
                maintenant = timezone.now()
                Expedition.objects.filter(pk=self.expedition_id).update(statut='attribuee', updated_at=maintenant)
                Offre.objects.filter(expedition_id=self.expedition_id, statut='proposee') \
                    .exclude(pk=self.pk).update(statut='refusee', updated_at=maintenant)
