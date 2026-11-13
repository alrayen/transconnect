
from django import forms

from VehiculesApp.models import Vehicule


class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = "__all__"
        exclude = ['id', 'created_at', 'updated_at']
        labels = {'type_vehicule': 'Type de véhicule', 'capacite_kg': 'Capacité (kg)', 'proprietaire': 'Propriétaire'}
        widgets = {'immatriculation': forms.TextInput(attrs={'placeholder': '123 TU 4567'})}
