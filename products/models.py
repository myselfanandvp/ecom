from django.db import models
# Create your models here.


class Products(models.Model):
    name= models.CharField(max_length=255,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=4)
    stock=models.PositiveIntegerField()
    category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='products_images/',blank=True,null=True)
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def __str__(self)->str:
        return self.name