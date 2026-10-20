from django.contrib import admin
from django.utils.html import format_html

from OffresApp.models import Offre

import csv
from django.http import HttpResponse

@admin.action(description="Exporter la sélection en CSV")
def exporter_offres_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="offres.csv"'
    writer = csv.writer(response)
    writer.writerow(['reference_expedition', 'transporteur', 'prix', 'statut'])
    for offre in queryset.select_related('expedition', 'entreprise'):
        writer.writerow([offre.expedition.reference, offre.entreprise.raison_sociale, offre.prix, offre.statut])
    return response

class OffreAdmin(admin.ModelAdmin):
    list_display = ('id', 'expedition', 'entreprise', 'vehicule', 'prix', 'statut_colore', 'created_at', 'updated_at')
    search_fields = ('expedition__reference', 'entreprise__raison_sociale', 'vehicule__immatriculation')
    list_filter = ('statut', 'created_at', 'updated_at')
    list_editable = ('prix',)
    ordering = ('-created_at',)
    list_per_page = 10
    date_hierarchy = 'date_proposition'
    readonly_fields = ('created_at', 'updated_at')
    autocomplete_fields = ('expedition', 'entreprise', 'vehicule')
    actions = [exporter_offres_csv]

    @admin.display(description='Statut')
    def statut_colore(self, obj):
        couleurs = {
            'proposee': '#F0AD4E',
            'acceptee': '#5CB85C',
            'refusee': '#D9534F',
        }
        return format_html(
            '<span style="color:white;background:{};padding:3px 8px;border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, '#999'), obj.get_statut_display(),
        )

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