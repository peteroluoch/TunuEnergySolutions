from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import CarbonCredit

class CarbonCreditsInfoView(TemplateView):
    """
    View to display information about carbon credits.
    """
    template_name = 'carbon_credits/carbon_credits_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Carbon Credits - Tunu Clean Energy'
        return context

class CarbonCalculatorView(TemplateView):
    """
    View with a calculator to estimate carbon credits based on energy production.
    """
    template_name = 'carbon_credits/carbon_calculator.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Carbon Credit Calculator - Tunu Clean Energy'
        return context

class MarketplaceView(ListView):
    """
    View to display the carbon credits marketplace.
    """
    model = CarbonCredit
    template_name = 'carbon_credits/marketplace.html'
    context_object_name = 'available_credits'

    def get_queryset(self):
        return CarbonCredit.objects.filter(is_available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Carbon Credits Marketplace - Tunu Clean Energy'
        return context
