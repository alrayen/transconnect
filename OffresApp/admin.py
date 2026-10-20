from django.contrib import admin

from OffresApp.models import Offre

class OffreAdmin(admin.ModelAdmin):
    list_display = ('id', 'expedition', 'entreprise', 'vehicule', 'created_at', 'updated_at')
    search_fields = ('expedition__reference', 'entreprise__raison_sociale', 'vehicule__immatriculation')
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations générales', {
            'fields': ('expedition', 'entreprise', 'vehicule', 'prix', 'delai_jours', 'date_proposition', 'statut')
        }),
        ('Informations de création', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
# Register your models here.
admin.site.register(Offre, OffreAdmin)