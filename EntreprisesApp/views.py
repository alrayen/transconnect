from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

from EntreprisesApp.models import Entreprise
from ExpeditionsApp.models import Expedition
from OffresApp.models import Offre
from VehiculesApp.models import Vehicule


@staff_member_required
def dashboard(request):
    context = {
        'nb_entreprises': Entreprise.objects.count(),
        'nb_expeditions': Expedition.objects.count(),
        'nb_publiees': Expedition.objects.filter(statut='publiee').count(),
        'nb_en_cours': Expedition.objects.filter(statut='en cours').count(),
        'nb_attribuees': Expedition.objects.filter(statut='attribuee').count(),
        'nb_terminees': Expedition.objects.filter(statut='terminee').count(),
        'nb_offres': Offre.objects.count(),
        'nb_proposees': Offre.objects.filter(statut='proposee').count(),
        'nb_vehicules': Vehicule.objects.count(),
        'nb_vehicules_dispo': Vehicule.objects.filter(disponible=True).count(),
        'dernieres_expeditions': Expedition.objects.order_by('-created_at')[:5],
    }
    return render(request, 'admin/dashboard.html', context)

# Create your views here.
