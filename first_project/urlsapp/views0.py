from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    s="<h1>hyderabd job info</h1>"
    return HttpResponse(s);
def fun2(request):
    s="<h1>kolkata job info</h1>"
    return HttpResponse(s);
