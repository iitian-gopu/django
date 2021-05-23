from django.shortcuts import render
from testapp.models import filtermodel
# Create your views here.

def upper_view(request):
    datalist=filtermodel.objects.all()
    return render(request, 'testapp/upper.html', context={'datalist':datalist})

def lower_view(request):
    datalist=filtermodel.objects.all()
    return render(request, 'testapp/lower.html', context={'datalist':datalist})

def truncate_view(request):
    datalist=filtermodel.objects.all()
    return render(request, 'testapp/truncate.html', context={'datalist':datalist})
