from django.shortcuts import render

# Create your views here.

def indexpage(request):
    return render(request,"index.html",{})

def homepage(request):
    return render(request,'homepage.html',{})

def loginpage(request):
    return render(request,'login.html',{})



def signup_page(request):
    return render(request,'signup.html',{})

