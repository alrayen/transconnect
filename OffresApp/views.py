from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from OffresApp.models import Offre
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
class Offre_delete(DeleteView):
    model = Offre
    template_name = 'offre/confirm_delete.html'
    context_object_name = 'off'
    success_url = reverse_lazy('offre_list')
class Offre_create(CreateView):
    model = Offre
    template_name = 'offre/forms.html'
    success_url = reverse_lazy('offre_list')
    form_class = OffreForm
class Offre_update(UpdateView):
    model = Offre
    template_name = 'offre/forms.html'
    success_url = reverse_lazy('offre_list')
    form_class = OffreForm
