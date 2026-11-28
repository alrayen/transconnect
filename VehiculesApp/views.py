from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from EntreprisesApp.mixins import TransporteurRequisMixin
from VehiculesApp.models import Vehicule
from .forms import VehiculeForm

# Create your views here.

class Vehicule_list(ListView):
    model = Vehicule
    template_name = 'vehicule/list.html'
    context_object_name = 'liste'

class Vehicule_detail(DetailView):
    model = Vehicule
    template_name = 'vehicule/detail.html'
    context_object_name = 'veh'

class VehiculesDeMonEntrepriseMixin:
    def get_queryset(self):
        return Vehicule.objects.filter(proprietaire=self.request.user.entreprise)

class Vehicule_delete(TransporteurRequisMixin, VehiculesDeMonEntrepriseMixin, DeleteView):
    model = Vehicule
    template_name = 'vehicule/confirm_delete.html'
    context_object_name = 'veh'
    success_url = reverse_lazy('vehicules:vehicule_list')
class Vehicule_create(TransporteurRequisMixin, CreateView):
    model = Vehicule
    template_name = 'vehicule/forms.html'
    success_url = reverse_lazy('vehicules:vehicule_list')
    form_class = VehiculeForm

    def form_valid(self, form):
        form.instance.proprietaire = self.request.user.entreprise
        return super().form_valid(form)
class Vehicule_update(TransporteurRequisMixin, VehiculesDeMonEntrepriseMixin, UpdateView):
    model = Vehicule
    template_name = 'vehicule/forms.html'
    success_url = reverse_lazy('vehicules:vehicule_list')
    form_class = VehiculeForm
