from django.contrib import admin

from EntreprisesApp.models import Entreprise, Utilisateur

class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('raison_sociale', 'type_entreprise', 'gerant', 'created_at', 'updated_at')
    search_fields = ('raison_sociale', 'type_entreprise', 'gerant__username')
    list_filter = ('type_entreprise', 'created_at', 'updated_at')
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

admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(Utilisateur)
