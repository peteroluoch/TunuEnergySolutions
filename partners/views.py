from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, FormView
from django.urls import reverse_lazy
from .models import Partner
from .forms import PartnerApplicationForm

class PartnerInfoView(TemplateView):
    """
    View to display information about becoming a partner.
    """
    template_name = 'partners/partner_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Partner with Tunu Clean Energy'
        return context

class PartnerApplicationView(FormView):
    """
    View with a form to apply to become a partner.
    """
    template_name = 'partners/partner_application.html'
    form_class = PartnerApplicationForm
    success_url = reverse_lazy('partners:partner_info')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your application has been submitted successfully!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Apply to Become a Partner - Tunu Clean Energy'
        return context

class DistributorsView(ListView):
    """
    View to display information about distributors.
    """
    model = Partner
    template_name = 'partners/distributors.html'
    context_object_name = 'distributors'

    def get_queryset(self):
        return Partner.objects.filter(partner_type='distributor', is_approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our Distributors - Tunu Clean Energy'
        return context

class NGOsView(ListView):
    """
    View to display information about NGO partners.
    """
    model = Partner
    template_name = 'partners/ngos.html'
    context_object_name = 'ngos'

    def get_queryset(self):
        return Partner.objects.filter(partner_type='ngo', is_approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Our NGO Partners - Tunu Clean Energy'
        return context
