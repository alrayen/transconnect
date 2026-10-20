from django.contrib import admin

from EntreprisesApp.models import Entreprise, Utilisateur
from VehiculesApp.models import Vehicule
from django.contrib.auth.admin import UserAdmin
admin.site.site_header = "Administration transconnect"
admin.site.site_title = "transconnect"
admin.site.index_title = "tableau de board de l'administration"
class VehiculeInline(admin.TabularInline):
    model = Vehicule
    extra = 1   
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible')
    show_change_link = True
class EntrepriseAdmin(admin.ModelAdmin):
    inlines = [VehiculeInline]
    list_display = ('raison_sociale', 'type_entreprise', 'gerant', 'created_at', 'updated_at')
    search_fields = ('raison_sociale', 'type_entreprise', 'gerant__username')
    list_filter = ('type_entreprise', 'created_at', 'updated_at')
    ordering = ('raison_sociale',)
    list_per_page = 10
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations générales', {
            'fields': ('raison_sociale', 'matricule_fiscale', 'type_entreprise', 'adresse', 'gerant')
        }),
        ('Informations de création', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'date_joined')
    ordering = ('-date_joined',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'telephone', 'role')}),
        ('Permissions', {'fields': ('is_active',)}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'telephone', 'usable_password', 'password1', 'password2'),
        }),
    )

admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(Utilisateur, UtilisateurAdmin)