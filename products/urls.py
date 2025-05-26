from django.urls import path
from .views import product_create,product_list
urlpatterns=[    
    path("create/",product_create,name='createproduct'),
    path("list/",product_list,name='productlist')
]