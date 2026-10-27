from django.urls import path

from .views import *

urlpatterns = [
    path('home/',home, name='home'),
    path('welcome/<str:name>/',welcome, name='welcome'),
    path('list/',listExpeditions, name='list'),
    path('detail/<int:pk>/',detailExpedition, name='detail'),
    path('delete/<int:pk>/',deleteExpedition, name='delete')
]