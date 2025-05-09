from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import InvestmentOpportunity

class InvestorInfoView(TemplateView):
    """
    View to display general information for investors.
    """
    template_name = 'investors/investor_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Investor Information - Tunu Clean Energy'
        return context

class InvestmentOpportunitiesView(ListView):
    """
    View to display current investment opportunities.
    """
    model = InvestmentOpportunity
    template_name = 'investors/investment_opportunities.html'
    context_object_name = 'opportunities'

    def get_queryset(self):
        return InvestmentOpportunity.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Investment Opportunities - Tunu Clean Energy'
        return context
