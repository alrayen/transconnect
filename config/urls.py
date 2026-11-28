"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from ExpeditionsApp.views import home
from EntreprisesApp.views import InscriptionView, profil, ProfilUpdateView
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('profil/', profil, name='profil'),
    path('profil/modifier/', ProfilUpdateView.as_view(), name='profil_modifier'),
    path('password_change/', PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('expeditions/', include('ExpeditionsApp.urls')),
    path('entreprises/', include('EntreprisesApp.urls')),
    path('vehicules/', include('VehiculesApp.urls')),
    path('offres/', include('OffresApp.urls')),
]
