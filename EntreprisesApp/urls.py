from django.urls import path

from .views import *

urlpatterns = [
    path('entreprises/', Entreprise_list.as_view(), name='entreprise_list'),
    path('entreprises/<int:pk>/', Entreprise_detail.as_view(), name='entreprise_detail'),
    path('entreprises/<int:pk>/delete/', Entreprise_delete.as_view(), name='entreprise_delete'),
    path('entreprises/create/', Entreprise_create.as_view(), name='entreprise_create'),
    path('entreprises/<int:pk>/update/', Entreprise_update.as_view(), name='entreprise_update')
]
