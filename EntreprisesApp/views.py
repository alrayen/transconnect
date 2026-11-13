from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView

from EntreprisesApp.models import Entreprise
from .forms import EntrepriseForm

# Create your views here.

class Entreprise_list(ListView):
    model = Entreprise
    template_name = 'entreprise/list.html'
    context_object_name = 'liste'

class Entreprise_detail(DetailView):
    model = Entreprise
    template_name = 'entreprise/detail.html'
    context_object_name = 'ent'
class Entreprise_delete(DeleteView):
    model = Entreprise
    template_name = 'entreprise/confirm_delete.html'
    context_object_name = 'ent'
    success_url = reverse_lazy('entreprise_list')
class Entreprise_create(CreateView):
    model = Entreprise
    template_name = 'entreprise/forms.html'
    success_url = reverse_lazy('entreprise_list')
    form_class = EntrepriseForm
class Entreprise_update(UpdateView):
    model = Entreprise
    template_name = 'entreprise/forms.html'
    success_url = reverse_lazy('entreprise_list')
    form_class = EntrepriseForm
