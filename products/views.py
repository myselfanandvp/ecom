from django.shortcuts import render,redirect
from .forms import ProductForm
# Create your views here.


def product_create(request):
    if request.POST:
        newproduct = ProductForm(request.POST,request.FILES)
        if newproduct.is_valid():
            newproduct.save()
            return redirect("productlist")
        print(newproduct.errors)
        return render(request,'product_create.html',{'productform':ProductForm(request.POST)})

    return render(request,'product_create.html',{'productform':ProductForm})



def product_list(request):
    return render(request,'productlist.html',{})