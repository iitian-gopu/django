from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"newsapp/index.html")

def movies(request):
    head_msg="Latest movie information"
    msg1="msg1"
    msg2="msg2"
    msg3="msg3"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render(request,"newsapp/news.html",context=my_dict)

def sports(request):
    head_msg="Latest sprts information"
    msg1="msg1"
    msg2="msg2"
    msg3="msg3"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render(request,"newsapp/news.html",context=my_dict)

def politics(request):
    head_msg="Latest politics information"
    msg1="msg1"
    msg2="msg2"
    msg3="msg3"
    my_dict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render(request,"newsapp/news.html",context=my_dict)
