from weakref import ref

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from EntreprisesApp.models import Entreprise
from .forms import ExpeditionForm

from .models import Expedition
from django.contrib.auth.decorators import login_required
from VehiculesApp.models import Vehicule
from OffresApp.models import Offre
# Create your views here.
@login_required
def home(request):
    context = {
        "nb_entreprises": Entreprise.objects.count(),
        "nb_vehicules": Vehicule.objects.count(),
        "nb_offres": Offre.objects.count(),
        "nb_expeditions": Expedition.objects.count(),
    }
    return render(request, "home.html", context)
def welcome(request,name):
    return HttpResponse(f"<h1>Bienvenue {name} sur la page d'accueil de l'application ExpeditionsApp</h1>")
def listExpeditions(request):
    list=Expedition.objects.all()
    return render(request,'expedition/list.html',{"liste":list})
def detailExpedition(request,pk):
    expedition=Expedition.objects.get(pk=pk)
    return render(request,'expedition/detail.html',{"exp":expedition})

def deleteExpedition(request,pk):
    expedition=Expedition.objects.get(pk=pk)
    expedition.delete()
    return redirect('list')

class Expedition_list(ListView):
    model = Expedition
    template_name = 'expedition/list.html'
    context_object_name = 'liste'

class Expedition_detail(DetailView):
    model = Expedition
    template_name = 'expedition/detail.html'
    context_object_name = 'exp'
class Expedition_delete(DeleteView):
    model = Expedition
    template_name = 'expedition/confirm_delete.html'
    context_object_name = 'exp'
    success_url = reverse_lazy('list')
class Expedition_create(CreateView):
    model = Expedition
    template_name = 'expedition/forms.html'
    success_url = reverse_lazy('list')
    #fields = ['ville_depart', 'ville_arrivee', 'poids_kg', 'date_souhaitee', 'description', 'entreprise']
    form_class = ExpeditionForm
class Expedition_update(UpdateView):
    model = Expedition
    template_name = 'expedition/forms.html'
    success_url = reverse_lazy('list')
    form_class = ExpeditionForm