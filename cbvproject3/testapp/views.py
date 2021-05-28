from django.shortcuts import render
from testapp.models import Company
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
# Create your views here.
class CompanyListView(ListView):
    model = Company

class CompanyDetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields=('name', 'location','ceo')

class CompanyUpdateView(UpdateView):
    model = Company
    fields=('location','ceo')  

class CompanyDeleteView(DeleteView):
    model = Company    
    success_url=reverse_lazy('company')  