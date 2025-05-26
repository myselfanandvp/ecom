from django.shortcuts import render,redirect
from django.contrib.auth.models import User
# Create your views here.



def indexpage(request):
    return render(request,"index.html",{"is_index":True})

def homepage(request):
    return render(request,'homepage.html',{})

def loginpage(request):
    return render(request,'login.html',{})



def signup_page(request):
    if request.POST:    
        email = request.POST.get('emailid','').strip()        
        phonenumber= request.POST.get('phonenumber','').strip()
        password=request.POST.get('password').strip()
        
        if email and phonenumber and password:
            newuser=User.objects.create(username=email,email=email,password=password)
            newuser.set_password(password)
            newuser.save()
            print("user saved")
            return  redirect('loginpage')
        else:
            return render(request,'signup.html',{})
    return render(request,'signup.html',{})

