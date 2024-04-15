from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLogin.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('profile/', ProfileTemplate.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
    path('', HomeTemplate.as_view(), name='index'),
    path('about/', AboutTemplate.as_view(), name='about'),
    path('buy-supplies/', SuppliesTemplate.as_view(), name='buy-supplies'),
    path('contact/', ContactTemplate.as_view(), name='contact'),
    path('projects/', ListingsTemplate.as_view(), name='projects'),
    path('project/', CreateProject.as_view(), name='project'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('project/<int:project_id>/bid/', ProjectBid.as_view(), name='project_bid'),
    path('contractors/', ContractorsTemplate.as_view(), name='contractors'),
]