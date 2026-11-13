
from django import forms

from OffresApp.models import Offre


class OffreForm(forms.ModelForm):
    class Meta:
        model = Offre
        fields = "__all__"
        exclude = ['id', 'created_at', 'updated_at']
        labels = {'delai_jours': 'Délai (jours)', 'date_proposition': 'Date de proposition', 'expedition': 'Expédition', 'entreprise': 'Transporteur', 'vehicule': 'Véhicule'}
        widgets = {'date_proposition': forms.DateInput(attrs={'type': 'date'},format='%Y-%m-%d')}
