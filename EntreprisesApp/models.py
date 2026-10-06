from time import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxLengthValidator, MinLengthValidator
# Create your models here.
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
matricule_fiscal_validator=RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$',message="format incorrect -ex(1234567AAM000 ou 1234567-A-A-M-000).")
def validate_email(value):
    if not value:
        raise ValidationError("L'adresse e-mail ne peut pas être vide.")
    if not value.endswith('@gmail.com'):
        raise ValidationError("L'adresse e-mail doit se terminer par '@gmail.com'.")
    
class Utilisateur(AbstractUser):
    user_id=models.CharField(max_length=8, primary_key=True)
    email=models.EmailField(unique=True, validators=[validate_email])
    role=models.CharField(max_length=20, choices=[
        ('admin','Administrateur'),
        ('char','Chargeur'),
        ('trans','Transporteur'),
    ], default='char')
    telephone=models.CharField(max_length=15, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    @classmethod
    def _generate_user_id(cls):
        annee = timezone.now().strftime('%y')
        prefix=f"{annee}user"
        dernier = cls.objects.filter(user_id__startswith=prefix).order_by('-user_id').first()
        compteur= int (dernier.user_id[-2:]) + 1 if dernier else 0
        if compteur > 99:
            raise ValidationError("Le compteur a dépassé la limite maximale de 99.")
        return f"{prefix}{compteur:02d}"
    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()
        self.full_clean()
        super().save(*args, **kwargs)
    

class Entreprise(models.Model):
    raison_sociale = models.CharField(max_length=200 , null=False, blank=False)
    matricule_fiscale = models.CharField(max_length=17, unique=True, validators=[matricule_fiscal_validator])
    type_entreprise = models.CharField(max_length=100, choices= [
        ('char','chargeur'),
        ('trans','transporteur'),
    ] , default='char')
    adresse =models.TextField(validators=[MinLengthValidator(20, "Adresse doit contenir au moins 10 caractères"), MaxLengthValidator(200, "Adresse ne doit pas dépasser 200 caractères")])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gerant = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='entreprise')
    
    


