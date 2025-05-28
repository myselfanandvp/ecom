from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import Customuser
from django.core.validators import RegexValidator


class SignupForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", 'placeholder': "Enter your email"}), required=True, label="Email"
    )
    phonenumber = forms.CharField(
        max_length=10, min_length=10, widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your phonenumber"}), required=True, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number  must be entered in the format: '+999999999'")])

    user_name = forms.CharField(max_length=250, widget=forms.TextInput(
        attrs={'class': "form-control", 'placeholder': "Enter your username"}), required=True, label="User Name"
    )
    profile_img = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': "Upload your profile image"}) ,label="Profile Photo" ,required=True  )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}),
        label="Password",
        required=True
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter your password"}),
        label="Confirm password",
        required=True
    )

    class Meta:
        model = Customuser
        fields = ['email', 'user_name',
                  'phonenumber', 'password1', 'password2','profile_img']

    def clean(self):
        clean_data = super().clean()
        password1 = clean_data.get('password1')
        password2 = clean_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "The two password fields didn't match.")
        return clean_data
            
    

        


class Loginform(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             "class": "form-control", "placeholder": "Enter your emailid"}), required=True, label="Email")
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={"class": "form-control", "placeholder": "Enter your password"}), required=True, label="Password")
