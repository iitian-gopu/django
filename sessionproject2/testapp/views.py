from django.shortcuts import render
from testapp.form import nameform
from testapp.form import ageform
from testapp.form import gfform

# Create your views here.
def nameview(request):
    form=nameform()
    return render(request,'testapp/name.html',{'form':form})

def ageview(request):
    name = request.GET['name']
    request.session['name']=name
    form=ageform()
    return render(request,'testapp/age.html',{'form':form})

def gfview(request):
    age = request.GET['age']
    request.session['age']=age
    form=gfform()
    return render(request,'testapp/gf.html',{'form':form})

def resultview(request):
    gf = request.GET['gf']
    age=request.session.get('age')
    name=request.session.get('name')

    return render(request,'testapp/result.html',{'name':name,'age':age,'gf':gf})
