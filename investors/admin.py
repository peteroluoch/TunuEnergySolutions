from django.contrib import admin
from .models import InvestmentOpportunity, Investor, InvestorInquiry

@admin.register(InvestmentOpportunity)
class InvestmentOpportunityAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount_needed', 'minimum_investment', 'is_active')
    list_filter = ('is_active', 'risk_level')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'organization', 'invested_amount', 'date_joined')
    list_filter = ('date_joined',)
    search_fields = ('full_name', 'email', 'organization')

@admin.register(InvestorInquiry)
class InvestorInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'company', 'opportunity', 'is_processed', 'created_at')
    list_filter = ('is_processed', 'created_at', 'opportunity')
    search_fields = ('name', 'email', 'company', 'message')
