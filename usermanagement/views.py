from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.



def indexpage(request):
    return render(request,"index.html",{"is_index":True})

def homepage(request):
    return render(request,'homepage.html',{})

def loginpage(request):
    if request.method=="POST":
        email=request.POST["emailid"].strip().lower()
        password= request.POST["password"].strip()
        if User.objects.filter(username=email).exists():
            return render(request,'loginpage.html',{"error":"User already exists"})
        newuser=User(username=email,email=email)
        newuser.set_password(password)
        newuser.is_staff=True
        newuser.save()
        print("user has been saved")
        return "User hasbeen saved"
        
    return render(request,'login.html',{})



def signup_page(request):
    return render(request,'signup.html',{})

