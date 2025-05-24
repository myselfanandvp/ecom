from django.urls import path
from .views import loginpage , signup_page,indexpage,homepage
urlpatterns = [
    path("",indexpage,name="indexpage"),
    path("login/",loginpage,name="loginpage"),
    path("signup/",signup_page,name="signuppage"),
    path("homepage/",homepage,name="homepage")
        
]