from django import forms
from .models import Products


class ProductForm(forms.ModelForm):

    CATEGORY_CHOICES = [('phone', 'Phone'),('books', 'Books'),('clothing', 'Clothing')  ]

    name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": 'form-control', 'placeholder': 'Enter the name of the product'})
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': "Enter the description here"})
    )
    price = forms.DecimalField(
        required=True,decimal_places=4,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Enter price'})
    )
    
    category= forms.ChoiceField(
        choices=CATEGORY_CHOICES
        ,widget=forms.Select(attrs={'class':'form-select'}),initial='phone'
    )

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),label="Product Image" )
    
    
    
    
    stock = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Available stock'})
        
    )

    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'stock','category','image']

