from django.shortcuts import render, redirect
from .forms import SignupForm, Loginform
from .models import Customuser
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
def indexpage(request):
    title="Index page"
    return render(request, "index.html", {"is_index": True,'title':title})


@never_cache
def loginpage(request):
    title="Login Page"
    if request.user.is_authenticated:
        return redirect("productlist")

    if request.method == "POST":
        login_form = Loginform(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            try:
                user = Customuser.objects.get(email=email)
            except Customuser.DoesNotExist as e:
                return render(request, 'login.html', {'loginform': login_form, 'error': 'User email is not valid !'})

            if user.check_password(password):
                login(request, user)
                print("Logged in")
                return redirect("productlist")
            else:
                return render(request, 'login.html', {
                    'loginform': login_form,
                    'error': 'Invalid password !'
                })
        else:
            return render(request, 'login.html', {'loginform': Loginform(request)})

    return render(request, 'login.html', {'loginform': Loginform(),"title":title})


@never_cache
def signup_page(request):
    title="Signup"
    if request.user.is_authenticated:
        return redirect('productlist')

    if request.method == "POST":
        form = SignupForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            print("user created")
            return redirect("loginpage")
        else:
            return render(request, 'signup.html', {'form': form, "title": title})

    form = SignupForm()
    return render(request, 'signup.html', {'form': form,"title":title})


@login_required
def logout_page(request):
    logout(request)
    request.session.flush()
    return redirect("loginpage")



