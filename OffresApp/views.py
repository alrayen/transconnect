from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from EntreprisesApp.mixins import TransporteurRequisMixin
from OffresApp.models import Offre
from VehiculesApp.models import Vehicule
from .forms import OffreForm

# Create your views here.

class Offre_list(ListView):
    model = Offre
    template_name = 'offre/list.html'
    context_object_name = 'liste'

class Offre_detail(DetailView):
    model = Offre
    template_name = 'offre/detail.html'
    context_object_name = 'off'

class OffresDeMonEntrepriseMixin:
    def get_queryset(self):
        return Offre.objects.filter(entreprise=self.request.user.entreprise)

class Offre_delete(TransporteurRequisMixin, OffresDeMonEntrepriseMixin, DeleteView):
    model = Offre
    template_name = 'offre/confirm_delete.html'
    context_object_name = 'off'
    success_url = reverse_lazy('offres:offre_list')
class Offre_create(TransporteurRequisMixin, CreateView):
    model = Offre
    template_name = 'offre/forms.html'
    success_url = reverse_lazy('offres:offre_list')
    form_class = OffreForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.instance.entreprise = self.request.user.entreprise
        form.fields['vehicule'].queryset = Vehicule.objects.filter(proprietaire=self.request.user.entreprise)
        return form
class Offre_update(TransporteurRequisMixin, OffresDeMonEntrepriseMixin, UpdateView):
    model = Offre
    template_name = 'offre/forms.html'
    success_url = reverse_lazy('offres:offre_list')
    form_class = OffreForm
