from django.urls import path
from .views import customLogin, homeIndex

urlpatterns = [
    path('', homeIndex, name='index'),
    path('login/', customLogin, name='login')
]