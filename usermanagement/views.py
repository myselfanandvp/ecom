from django.shortcuts import render,redirect
from .forms import SignupForm,Loginform
from .models import Customuser
from django.contrib.auth import login,logout
# Create your views here.



def indexpage(request):
    return render(request,"index.html",{"is_index":True})

def loginpage(request):
    if request.method=="POST":
        login_form = Loginform(request.POST)
        if login_form.is_valid():
            email=login_form.cleaned_data['email']
            password=login_form.cleaned_data['password']
            user=Customuser.objects.get(email=email)
            if user.check_password(password):
                login(request,user)
                print("Logged in")
                return redirect("homepage")
        else:
            return render(request,'login.html',{'loginform':Loginform(request)})
        
    return render(request,'login.html',{'loginform':Loginform()})



def signup_page(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        
        if form.is_valid():        
            form.save()
            print("user created")
            return redirect("loginpage")
        else:
            return render(request,'signup.html',{'form':SignupForm(request.POST)})
            
    form = SignupForm()       
    return render(request,'signup.html',{'form':form})


def logout_page(request):
    logout(request)
    return redirect("loginpage")

