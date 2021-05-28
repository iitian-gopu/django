from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse
# Create your views here.
class Helloview(View):
    def get(self,request):
        return HttpResponse('<h1>Class Bsed View</h1')

class Hellotempview(TemplateView):
    template_name='testapp/result.html' 

class Hellotempcontext(TemplateView):
    template_name='testapp/info.html' 

    def get_context_data(self,**kwargs):
     context=super().get_context_data(**kwargs)
     context['name']='gopal' 
     context['age']='21'            
     context['marks']='100'
     return context            
