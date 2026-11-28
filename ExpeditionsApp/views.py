from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from EntreprisesApp.mixins import ChargeurRequisMixin
from EntreprisesApp.models import Entreprise
from .forms import ExpeditionForm

from .models import Expedition
from VehiculesApp.models import Vehicule
from OffresApp.models import Offre
# Create your views here.
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


class Expedition_list(ListView):
    model = Expedition
    template_name = 'expedition/list.html'
    context_object_name = 'liste'

class Expedition_detail(DetailView):
    model = Expedition
    template_name = 'expedition/detail.html'
    context_object_name = 'exp'

class ExpeditionsDeMonEntrepriseMixin:
    def get_queryset(self):
        return Expedition.objects.filter(entreprise=self.request.user.entreprise)

class Expedition_delete(ChargeurRequisMixin, ExpeditionsDeMonEntrepriseMixin, DeleteView):
    model = Expedition
    template_name = 'expedition/confirm_delete.html'
    context_object_name = 'exp'
    success_url = reverse_lazy('expeditions:list')
class Expedition_create(ChargeurRequisMixin, CreateView):
    model = Expedition
    template_name = 'expedition/forms.html'
    success_url = reverse_lazy('expeditions:list')
    form_class = ExpeditionForm

    def form_valid(self, form):
        form.instance.entreprise = self.request.user.entreprise
        return super().form_valid(form)
class Expedition_update(ChargeurRequisMixin, ExpeditionsDeMonEntrepriseMixin, UpdateView):
    model = Expedition
    template_name = 'expedition/forms.html'
    success_url = reverse_lazy('expeditions:list')
    form_class = ExpeditionForm
