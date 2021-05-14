from django.conf.urls import url
from testapp import views
urlpatterns = [
    
    url(r'^test/', views.fun1),
]
