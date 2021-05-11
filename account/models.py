from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string


class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra):
        if not email:
            raise ValueError('Email is not provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.create_activation_code()
        user.save()
        return user

    def create_superuser(self, email, password, **extra):
        if not email:
            raise ValueError('Email is not provided')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user


class MyUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=20, blank=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def create_activation_code(self):
        code = get_random_string(length=20, allowed_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        self.activation_code = code

