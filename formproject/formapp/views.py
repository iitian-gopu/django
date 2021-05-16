from django.shortcuts import render
from . import forms
# Create your views here.
def register(request):
    form = forms.Student()
    return render(request, 'formapp/register.html', {'form':form})
