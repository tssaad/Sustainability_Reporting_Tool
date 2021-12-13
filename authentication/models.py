from institute.models import Institute

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db.models.base import Model
from django.core.validators import RegexValidator

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('Username is needed')
        if email is None:
            raise TypeError('Email is needed')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError('Password is needed')

        user = self.create_user(username, email, password) # this will do the same as self.model and user.set_password
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username=models.TextField(max_length=255, unique=True, db_index=True)
    email=models.EmailField(max_length=255, unique=True, db_index=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    img = models.ImageField(upload_to="users/", blank=True, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="e.g.: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(max_length=25, validators=[phone_regex], blank=True, null=True)

    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.email

