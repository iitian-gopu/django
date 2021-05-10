from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    s="urlapp fun1"
    return HttpResponse(s)
def fun2(request):
    s="urlapp fun2"
    return HttpResponse(s)
