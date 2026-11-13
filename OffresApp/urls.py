from django.urls import path

from .views import *

urlpatterns = [
    path('offres/', Offre_list.as_view(), name='offre_list'),
    path('offres/<int:pk>/', Offre_detail.as_view(), name='offre_detail'),
    path('offres/<int:pk>/delete/', Offre_delete.as_view(), name='offre_delete'),
    path('offres/create/', Offre_create.as_view(), name='offre_create'),
    path('offres/<int:pk>/update/', Offre_update.as_view(), name='offre_update')
]
