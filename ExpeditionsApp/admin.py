from django.contrib import admin

from ExpeditionsApp.models import Expedition
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'poids_kg', 'statut', 'created_at', 'updated_at', 'entreprise')
    search_fields = ('reference', 'statut', 'entreprise__raison_sociale')
    list_filter = ('statut', 'created_at', 'updated_at')
    list_per_page = 5
    list_editable = ('statut',)
    ordering = ('-created_at',)
    readonly_fields = ('reference', 'created_at', 'updated_at')
    fieldsets = (
        ('Informations générales', {
            'fields': ('poids_kg', 'statut', 'ville_depart', 'ville_arrivee')
        }),
        ('Informations de création', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
# Register your models here.
admin.site.register(Expedition, ExpeditionAdmin)