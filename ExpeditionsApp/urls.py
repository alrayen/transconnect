from django.urls import path

from .views import *

urlpatterns = [
    path('welcome/<str:name>/',welcome, name='welcome'),
    path('list/',listExpeditions, name='list'),
    path('detail/<int:pk>/',detailExpedition, name='detail'),
    path('delete/<int:pk>/',deleteExpedition, name='delete'),
    path('expeditions/', Expedition_list.as_view(), name='expedition_list'),
    path('expeditions/<int:pk>/', Expedition_detail.as_view(), name='expedition_detail'),
    path('expeditions/<int:pk>/delete/', Expedition_delete.as_view(), name='expedition_delete'),
    path('expeditions/create/', Expedition_create.as_view(), name='expedition_create'),
    path('expeditions/<int:pk>/update/', Expedition_update.as_view(), name='expedition_update')
]