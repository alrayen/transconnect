from django.contrib import admin

from VehiculesApp.models import Vehicule
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible', 'proprietaire', 'created_at', 'updated_at')
    search_fields = ('immatriculation', 'type_vehicule', 'proprietaire__raison_sociale')
    list_filter = ('type_vehicule', 'disponible', 'created_at', 'updated_at')
    list_editable = ('disponible',)
    ordering = ('-created_at',)
    list_per_page = 5
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations générales', {
            'fields': ('immatriculation', 'type_vehicule', 'capacite_kg', 'disponible', 'proprietaire')
        }),
        ('Informations de création', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
# Register your models here.
admin.site.register(Vehicule, VehiculeAdmin)