from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.http import HttpResponse

def homeIndex(request):
    return render(request, 'base/index.html')

# def customLogin(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('index')
#     return render(request, 'base/login.html')

class HomeTemplate(TemplateView):
    template_name = 'base/index.html'

class AboutTemplate(TemplateView):
    template_name = 'base/about.html'

class SuppliesTemplate(TemplateView):
    template_name = 'base/buy_supplies.html'

class ContactTemplate(TemplateView):
    template_name = 'base/contact.html'

class ListingsTemplate(TemplateView):
    template_name = 'base/contracts.html'

class ContractorsTemplate(TemplateView):
    template_name = 'base/contractors.html'

class LogTemplate(TemplateView):
    template_name = 'base/login.html'

class ProfileTemplate(TemplateView):
    template_name = 'base/profile.html'