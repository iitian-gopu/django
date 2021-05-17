from django.shortcuts import render
from testapp import forms
from testapp.models import movie
# Create your views here.
def indexview(request):
    return render(request,'testapp/index.html')

def addmovieview(request):
    form=forms.movieform()
    if request.method== 'POST':
        form = forms.movieform(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return indexview(request)
    return render(request,'testapp/add.html',{'form':form})


def listmovieview(request):
     movielist=movie.objects.all()
     return render(request,'testapp/list.html',{'movielist':movielist})
