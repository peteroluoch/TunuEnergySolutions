from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages

class HomeView(TemplateView):
    """
    Home page view for the Tunu Clean Energy website.
    """
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tunu Clean Energy - Portable Hydro Power Solutions'
        return context

class AboutView(TemplateView):
    """
    About page view with information about the company and technology.
    """
    template_name = 'core/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Tunu Clean Energy'
        return context

class ContactView(TemplateView):
    """
    Contact page view with contact form and information.
    """
    template_name = 'core/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Tunu Clean Energy'
        return context
