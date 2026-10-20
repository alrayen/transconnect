from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from ExpeditionsApp.models import Expedition
from OffresApp.models import Offre

class OffreInline(admin.TabularInline):
    model = Offre
    extra = 0
    fields = ('entreprise', 'vehicule', 'prix', 'delai_jours', 'statut')
    readonly_fields = ('entreprise', 'vehicule', 'prix', 'delai_jours', 'statut')
    can_delete = False
class EnRetardFilter(admin.SimpleListFilter):
    title = 'En retard'
    parameter_name = 'en_retard'

    def lookups(self, request, model_admin):
        return (
            ('oui', 'Oui'),
            ('non', 'Non'),
        )

    def queryset(self, request, queryset):
        aujourd_hui=timezone.now().date()
        if self.value() == 'oui':
            return queryset.filter(statut='publiee', date_souhaitee__lt=aujourd_hui)
        elif self.value() == 'non':
            return queryset.exclude(statut='publiee', date_souhaitee__lt=aujourd_hui)
        return queryset

class ExpeditionAdmin(admin.ModelAdmin):
    inlines = [OffreInline]
    list_display = ('reference', 'poids_kg', 'statut', 'statut_colore', 'created_at', 'updated_at', 'entreprise')
    search_fields = ('reference', 'statut', 'entreprise__raison_sociale')
    list_filter = ('statut', 'created_at', 'updated_at',EnRetardFilter)
    list_per_page = 5
    list_editable = ('statut',)
    ordering = ('-created_at',)
    date_hierarchy = 'date_souhaitee'
    readonly_fields = ('reference', 'created_at', 'updated_at')
    autocomplete_fields = ('entreprise',)

    @admin.display(description='Statut (badge)')
    def statut_colore(self, obj):
        couleurs = {
            'publiee': '#5BC0DE',
            'attribuee': '#F0AD4E',
            'en cours': '#337AB7',
            'terminee': '#5CB85C',
        }
        return format_html(
            '<span style="color:white;background:{};padding:3px 8px;border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, '#999'), obj.get_statut_display(),
        )

    fieldsets = (
        ('Informations générales', {
            'fields': ('entreprise', 'poids_kg', 'statut', 'ville_depart', 'ville_arrivee', 'date_souhaitee', 'description')
        }),
        ('Informations de création', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    actions = ['cloturer_expeditions']

    @admin.action(description="Clôturer les expéditions sélectionnées")
    def cloturer_expeditions(self, request, queryset):
        expeditions = queryset.filter(statut='en cours')
        nombre = 0
        for expedition in expeditions:
            expedition.statut = 'terminee'
            expedition.full_clean()
            expedition.save()
            nombre = nombre + 1
        self.message_user(request, f"{nombre} expédition(s) clôturée(s).")

# Register your models here.
admin.site.register(Expedition, ExpeditionAdmin)