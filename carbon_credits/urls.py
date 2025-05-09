from django.urls import path
from . import views

app_name = 'carbon_credits'

urlpatterns = [
    path('', views.CarbonCreditsInfoView.as_view(), name='carbon_credits_info'),
    path('calculator/', views.CarbonCalculatorView.as_view(), name='carbon_calculator'),
    path('marketplace/', views.MarketplaceView.as_view(), name='marketplace'),
]
