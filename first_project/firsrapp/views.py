from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcomefunction(request):
    s='<h1>Django is nursery level </h1>'
    return HttpResponse(s)
