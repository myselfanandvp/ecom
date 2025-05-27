from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Customusermanager(BaseUserManager):

    def create_user(self, email, phonenumber, user_name, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address"))
        if not phonenumber:
            raise ValueError(_("You must provide a phonenumber"))
        if not user_name:
            raise ValueError(_("You must provide an username"))

        email = self.normalize_email(email)
        user = self.model(email=email, phonenumber=phonenumber,user_name=user_name,password=password,**other_fields)
        user.set_password(password)
        other_fields.setdefault("is_staff", True)
        user.save()
        return user

    def create_superuser(self, email, phonenumber, user_name, password, **other_fields):        
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_superuser", True)
        if not other_fields.get('is_staff'):
            raise ValueError('Superuser must be assigned to is_staff=True.')
        if not other_fields.get('is_superuser'):
            raise ValueError(
                "Superuser must be assigned to is_superuser=True.")
        return self.create_user(email=email, phonenumber=phonenumber, user_name=user_name, password=password, **other_fields)


class Customuser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    phonenumber = models.CharField(_('phone_number'), unique=True)
    user_name = models.CharField(_('username'), max_length=150, unique=True)
    profile_img=models.ImageField(_("profile_image"),upload_to="profile_images/",blank=True,null=True)
    created_date = models.DateField(_('created_date'), default=timezone.now)
    is_staff = models.BooleanField(_('is_staff'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_superuser=models.BooleanField("is_superuser",default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phonenumber', 'user_name']

    objects = Customusermanager()
