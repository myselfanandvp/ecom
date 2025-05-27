from django.shortcuts import render,redirect
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from .models import Products
# Create your views here.

@login_required
def product_create(request):
    if request.POST:
        newproduct = ProductForm(request.POST,request.FILES)
        if newproduct.is_valid():
            newproduct.save()
            return redirect("productlist")
        print(newproduct.errors)
        return render(request,'product_create.html',{'productform':ProductForm(request.POST)})

    return render(request,'product_create.html',{'productform':ProductForm})


@login_required
def product_list(request):
    products=Products.objects.all()
    return render(request,'productlist.html',{'products':products})