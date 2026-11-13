from django.urls import path

from .views import *

urlpatterns = [
    path('vehicules/', Vehicule_list.as_view(), name='vehicule_list'),
    path('vehicules/<int:pk>/', Vehicule_detail.as_view(), name='vehicule_detail'),
    path('vehicules/<int:pk>/delete/', Vehicule_delete.as_view(), name='vehicule_delete'),
    path('vehicules/create/', Vehicule_create.as_view(), name='vehicule_create'),
    path('vehicules/<int:pk>/update/', Vehicule_update.as_view(), name='vehicule_update')
]
