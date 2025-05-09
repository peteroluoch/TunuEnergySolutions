from django.contrib import admin
from .models import CarbonCreditProject, CarbonCredit, CarbonCreditTransaction

@admin.register(CarbonCreditProject)
class CarbonCreditProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'location', 'energy_generated_mwh', 'co2_offset_tons', 'registered_date')
    list_filter = ('location', 'registered_date')
    search_fields = ('project_name', 'location')
    date_hierarchy = 'registered_date'

@admin.register(CarbonCredit)
class CarbonCreditAdmin(admin.ModelAdmin):
    list_display = ('credit_id', 'project', 'amount', 'price_per_ton', 'is_available')
    list_filter = ('is_available', 'verification_standard', 'project')
    search_fields = ('credit_id', 'project__project_name')
    date_hierarchy = 'created_at'

@admin.register(CarbonCreditTransaction)
class CarbonCreditTransactionAdmin(admin.ModelAdmin):
    list_display = ('carbon_credit', 'transaction_type', 'amount', 'price_per_ton', 'transaction_date')
    list_filter = ('transaction_type', 'transaction_date')
    search_fields = ('carbon_credit__credit_id', 'buyer__username', 'seller__username')
    date_hierarchy = 'transaction_date'
