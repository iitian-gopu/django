from django.shortcuts import render

# Create your views here.
def homeview(request):
    return render(request,'testapp/home.html')

def moviesview(request):
    return render(request,'testapp/movies.html')

def sportsview(request):
    return render(request,'testapp/sports.html')

def politicsview(request):
    return render(request,'testapp/politics.html')
