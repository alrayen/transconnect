
from django import forms

from EntreprisesApp.models import Entreprise, Utilisateur


class EntrepriseForm(forms.ModelForm):
    class Meta:
        model = Entreprise
        fields = "__all__"
        exclude = ['id', 'created_at', 'updated_at']
        labels = {'type_entreprise': "Type d'entreprise", 'gerant': 'Gérant'}
        widgets = {
            'matricule_fiscale': forms.TextInput(attrs={'placeholder': '1234567AAM000'}),
            'adresse': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            self.fields['gerant'].queryset = Utilisateur.objects.filter(entreprise__isnull=True)
