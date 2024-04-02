from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views import View
from django.urls import reverse_lazy
from .models import Project

from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView

class LoginView(View):
    template_name = 'base/login.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        if 'login_form' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, self.template_name, {'error_message': 'Invalid username or password'})
        
        elif 'register_form' in request.POST:
            username = request.POST.get('reg_username')
            email = request.POST.get('email')
            password = request.POST.get('reg_password')
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                return render(request, self.template_name, {'error_message': 'Username or email already exists. Please enter a different one.'})
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                login(request, new_user)
                return redirect('index')
        else:
            return render(request, self.template_name)

class HomeTemplate(TemplateView):
    template_name = 'base/index.html'

class AboutTemplate(TemplateView):
    template_name = 'base/about.html'

class SuppliesTemplate(TemplateView):
    template_name = 'base/buy_supplies.html'

class ContactTemplate(TemplateView):
    template_name = 'base/contact.html'

class ListingsTemplate(ListView):
    template_name = 'base/contracts.html'

class ContractorsTemplate(TemplateView):
    template_name = 'base/contractors.html'

class ProfileTemplate(TemplateView):
    template_name = 'base/profile.html'