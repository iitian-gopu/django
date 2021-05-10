from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def fun1(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    s="Hello very";
    if h<12:
        s+="good morngin"
    elif h<16:
          s+="good afternoon"
    elif h<17:
           s+="good evening"
    else:
         s+="good night"
    s+='<hr>'
    s+="<h1>TIME is:"+str(date)+""
    return HttpResponse(s)
