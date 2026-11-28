
from django import forms

from VehiculesApp.models import Vehicule


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = ['immatriculation', 'type_vehicule', 'capacite_kg', 'disponible']
        labels = {'type_vehicule': 'Type de véhicule', 'capacite_kg': 'Capacité (kg)'}
        widgets = {'immatriculation': forms.TextInput(attrs={'placeholder': '123 TU 4567'})}
