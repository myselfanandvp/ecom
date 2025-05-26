from django.urls import path
from .views import loginpage , signup_page,indexpage,logout_page
urlpatterns = [
    path("",indexpage,name="indexpage"),
    path("login/",loginpage,name="loginpage"),
    path("register/",signup_page,name="signuppage"),
    path("logout/",logout_page,name="logout"),
        
]