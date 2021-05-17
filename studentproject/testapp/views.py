from django.shortcuts import render
from testapp import forms
# Create your views here.
def studentview(request):
    form = forms.studentform()
    if request.method== 'POST':
        form = forms.studentform(request.POST)
        if form.is_valid():
            form.save(commit=True)
    return render(request,'testapp/register.html',{'form':form})
