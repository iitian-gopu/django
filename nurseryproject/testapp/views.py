from django.shortcuts import render
import datetime
# Create your views here.
def fun1(request):
    date=datetime.datetime.now()
    hr=int((date.strftime('%H')))
    msg=""
    if hr<12:
        msg+="Good morning"
    elif hr<16:
        msg+="Good afternoon"
    elif hr<17:
        msg+="Good evening"
    else:
        msg+="Good night"
    name='sunny'
    my_dict={'date':date,'name':name,'msg':msg}

    return render(request, 'testapp/test.html',context=my_dict)
