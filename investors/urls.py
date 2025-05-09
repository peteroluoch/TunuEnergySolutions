from django.urls import path
from . import views

app_name = 'investors'

urlpatterns = [
    path('', views.InvestorInfoView.as_view(), name='investor_info'),
    path('opportunities/', views.InvestmentOpportunitiesView.as_view(), name='investment_opportunities'),
]
