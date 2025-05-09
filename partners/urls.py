from django.urls import path
from . import views

app_name = 'partners'

urlpatterns = [
    path('', views.PartnerInfoView.as_view(), name='partner_info'),
    path('apply/', views.PartnerApplicationView.as_view(), name='partner_application'),
    path('distributors/', views.DistributorsView.as_view(), name='distributors'),
    path('ngos/', views.NGOsView.as_view(), name='ngos'),
]
