from django.conf.urls import url
from urlsapp import views
urlpatterns = [
    url(r'^fun1/', views.fun1),
    url(r'^fun2/', views.fun2),
]
