from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from EntreprisesApp.models import Entreprise
from .forms import EntrepriseForm, InscriptionForm, ProfilForm


# Create your views here.

class Entreprise_list(ListView):
    model = Entreprise
    template_name = 'entreprise/list.html'
    context_object_name = 'liste'

class Entreprise_detail(DetailView):
    model = Entreprise
    template_name = 'entreprise/detail.html'
    context_object_name = 'ent'

class MonEntrepriseMixin:
    def get_queryset(self):
        return Entreprise.objects.filter(gerant=self.request.user)

class Entreprise_delete(LoginRequiredMixin, MonEntrepriseMixin, DeleteView):
    model = Entreprise
    template_name = 'entreprise/confirm_delete.html'
    context_object_name = 'ent'
    success_url = reverse_lazy('entreprises:entreprise_list')
class Entreprise_create(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Entreprise
    template_name = 'entreprise/forms.html'
    success_url = reverse_lazy('expeditions:expedition_list')
    form_class = EntrepriseForm

    def test_func(self):
        return getattr(self.request.user, 'entreprise', None) is None

    def form_valid(self, form):
        form.instance.gerant = self.request.user
        return super().form_valid(form)
class Entreprise_update(LoginRequiredMixin, MonEntrepriseMixin, UpdateView):
    model = Entreprise
    template_name = 'entreprise/forms.html'
    success_url = reverse_lazy('entreprises:entreprise_list')
    form_class = EntrepriseForm

class InscriptionView(CreateView):
    form_class = InscriptionForm
    template_name = 'inscription.html'
    success_url = reverse_lazy('entreprises:entreprise_create')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response

@login_required
def profil(request):
    return render(request, 'profil.html')

class ProfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProfilForm
    template_name = 'profil_form.html'
    success_url = reverse_lazy('profil')

    def get_object(self, queryset=None):
        return self.request.user
