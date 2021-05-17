from django.shortcuts import render
from feedapp import forms
# Create your views here.
def feedback(request):
    form = forms.feedback()
    if request.method=='POST':
        form = forms.feedback(request.POST)
    if form.is_valid():
        print('Successfully')
        print(form.cleaned_data['name'])
        print(form.cleaned_data['rollno'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['feedback'])
        return render(request, 'feedapp/feedback.html', {'form':form})
    return render(request, 'feedapp/feedback.html', {'form':form})
