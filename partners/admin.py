from django.contrib import admin
from .models import Partner

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'email', 'region', 'is_verified', 'joined_on')
    list_filter = ('is_verified', 'partner_type', 'region')
    search_fields = ('name', 'contact_person', 'email', 'region')
    date_hierarchy = 'joined_on'
