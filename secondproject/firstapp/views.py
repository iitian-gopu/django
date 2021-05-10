from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def greeting(request):
    date=datetime.datetime.now()
    msg='<h1>Hello Goodevening </h1>'
    msg+='<h1>Time is:'+str(date) +'</h1>'
    return HttpResponse(msg)
