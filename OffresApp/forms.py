
from django import forms

from OffresApp.models import Offre


class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = ['expedition', 'vehicule', 'prix', 'delai_jours', 'date_proposition']
        labels = {'delai_jours': 'Délai (jours)', 'date_proposition': 'Date de proposition', 'expedition': 'Expédition', 'vehicule': 'Véhicule'}
        widgets = {'date_proposition': forms.DateInput(attrs={'type': 'date'},format='%Y-%m-%d')}
