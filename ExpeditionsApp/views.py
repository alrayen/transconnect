from weakref import ref

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Expedition
# Create your views here.
def home(request):
    return HttpResponse("<h1>Bienvenue sur la page d'accueil de l'application ExpeditionsApp</h1>")
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