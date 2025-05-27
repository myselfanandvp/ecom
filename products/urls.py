from django.urls import path
from .views import product_create,product_list,editproduct,delete_product

urlpatterns=[    
    path("create/",product_create,name='createproduct'),
    path("list/",product_list,name='productlist'),
    path("edit/<int:product_id>/",editproduct,name='editproducturl'),
    path("delete/<int:product_id>/",delete_product,name='deleteproducturl'),
]

