from django.contrib import admin

from EntreprisesApp.models import Entreprise, Utilisateur

class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('raison_sociale', 'type_entreprise', 'gerant', 'created_at', 'updated_at')
    search_fields = ('raison_sociale', 'type_entreprise', 'gerant__username')
    list_filter = ('type_entreprise', 'created_at', 'updated_at')

admin.site.register(Entreprise, EntrepriseAdmin)
admin.site.register(Utilisateur)
