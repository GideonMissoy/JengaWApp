from django.urls import path
from .views import HomeTemplate, AboutTemplate, SuppliesTemplate, ContactTemplate,  ListingsTemplate, ContractorsTemplate, LogTemplate, ProfileTemplate

urlpatterns = [
    path('', HomeTemplate.as_view(), name='index'),
    path('about/', AboutTemplate.as_view(), name='about'),
    path('buy-supplies/', SuppliesTemplate.as_view(), name='buy-supplies'),
    path('contact/', ContactTemplate.as_view(), name='contact'),
    path('contracts/', ListingsTemplate.as_view(), name='contracts'),
    path('contractors/', ContractorsTemplate.as_view(), name='contractors'),
    path('login/', LogTemplate.as_view(), name='login'),
    path('profile/', ProfileTemplate.as_view(), name='profile'),
]