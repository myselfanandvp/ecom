from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from .models import Products
import os
from django.conf import settings
from django.views.decorators.cache import never_cache
# Create your views here.

@never_cache
@login_required
def product_create(request):
    if request.method == "POST":
        newproduct = ProductForm(request.POST, request.FILES)
        if newproduct.is_valid():
            newproduct.save()
            return redirect("productlist")
        print(newproduct.errors)
        return render(request, 'product_create.html', {'productform': newproduct})

    return render(request, 'product_create.html', {'productform': ProductForm()})

@never_cache
@login_required
def product_list(request):
    products = Products.objects.all()
    recent_edit = request.session.get('recent_edit', [])
    recentedited = Products.objects.filter(id__in=recent_edit)
    return render(request, 'productlist.html', {'products': products, 'recent_edited': recentedited})

@never_cache
@login_required
def editproduct(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    recent_edit = request.session.get('recent_edit', [])
    if product_id in recent_edit:
        recent_edit.remove(product_id)

    recent_edit.insert(0,int(product_id))

    recent_edit = recent_edit[:3]
    
    request.session['recent_edit'] = recent_edit
    
    if request.method == "POST" and product:
        updated_form = ProductForm(
            request.POST, request.FILES, instance=product)
        if updated_form.is_valid():
            updated_form.save()
            return redirect("productlist")

    form = ProductForm(instance=product)

    return render(request, 'product_edit.html', {'editform': form})


@login_required
def delete_product(request, product_id):
    obj = get_object_or_404(Products, id=product_id)
    if obj.image:
        image_path = os.path.join(settings.MEDIA_ROOT, obj.image.name)
        if os.path.exists(image_path):
            os.remove(image_path)
    obj.delete()
    return redirect("productlist")
