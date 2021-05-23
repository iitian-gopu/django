from django.shortcuts import render
from testapp.forms import Additemform
# Create your views here.
def add_itemview(request):
    form=Additemform()
    if request.method=='POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(120)
    return render(request, 'testapp/add.html', {'form':form})

def display_itemview(request):
    return render(request, 'testapp/display.html')
