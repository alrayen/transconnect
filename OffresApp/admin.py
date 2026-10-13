from django.contrib import admin

from OffresApp.models import Offre

class OffreAdmin(admin.ModelAdmin):
    list_display = ('id', 'expedition', 'entreprise', 'vehicule', 'created_at', 'updated_at')
    search_fields = ('expedition__reference', 'entreprise__raison_sociale', 'vehicule__immatriculation')
    list_filter = ('created_at', 'updated_at')
# Register your models here.
admin.site.register(Offre, OffreAdmin)