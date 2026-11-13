from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

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
class Vehicule_delete(DeleteView):
    model = Vehicule
    template_name = 'vehicule/confirm_delete.html'
    context_object_name = 'veh'
    success_url = reverse_lazy('vehicule_list')
class Vehicule_create(CreateView):
    model = Vehicule
    template_name = 'vehicule/forms.html'
    success_url = reverse_lazy('vehicule_list')
    form_class = VehiculeForm
class Vehicule_update(UpdateView):
    model = Vehicule
    template_name = 'vehicule/forms.html'
    success_url = reverse_lazy('vehicule_list')
    form_class = VehiculeForm
