from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.views.generic import TemplateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from .models import Project, Bid

class CustomLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')
    print("Some text to confirm.", form_class)

    def form_valid(self, form):
        user =form.save()
        print('This is a new user: ', user)
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
class HomeTemplate(TemplateView):
    template_name = 'base/index.html'

class ListingsTemplate(ListView):
    model = Project
    context_object_name = 'projects'
    template_name = 'base/projects.html'

class ProjectDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'base/project_detail.html'

class CreateProject(CreateView):
    model = Project
    fields = '__all__'
    template_name = 'base/project_form.html'
    success_url = reverse_lazy('projects')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProject, self).form_valid (form)


class BidsTemplate(ListView):
    model = Bid
    context_object_name = 'bids'
    template_name = 'base/bids.html'

class ProjectBid(DetailView):
    model = Bid
    fields = '__all__'
    context_object_name = 'bid'
    template_name = 'base/project_bid.html'

class ContractorsTemplate(TemplateView):
    template_name = 'base/contractors.html'

class SuppliesTemplate(TemplateView):
    template_name = 'base/buy_supplies.html'

class AboutTemplate(TemplateView):
    template_name = 'base/about.html'

class ContactTemplate(TemplateView):
    template_name = 'base/contact.html'

class ProfileTemplate(TemplateView):
    template_name = 'base/profile.html'