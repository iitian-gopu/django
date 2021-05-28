from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from testapp.models import Book
# Create your views here.
class BookListView(ListView):
    model = Book
    

class DetailListView(DetailView):
    model = Book
