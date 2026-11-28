
from django import forms

from EntreprisesApp.models import Entreprise, Utilisateur

from django.contrib.auth.forms import UserCreationForm
class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = ['raison_sociale', 'matricule_fiscale', 'type_entreprise', 'adresse']
        labels = {'type_entreprise': "Type d'entreprise"}
        widgets = {
            'matricule_fiscale': forms.TextInput(attrs={'placeholder': '1234567AAM000'}),
            'adresse': forms.Textarea(attrs={'rows': 3}),
        }

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'email', 'telephone']

class InscriptionForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = ('username', 'email', 'telephone')
