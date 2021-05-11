from django.shortcuts import render
import datetime
# Create your views here.
def fun1(request):
    date=datetime.datetime.now()
    dict={'date_msg':date}
    return render(request, 'testapp/wish.html',context=dict)
