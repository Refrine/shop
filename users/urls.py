from django.urls import path
from shop.views import register

app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
   
    
]
