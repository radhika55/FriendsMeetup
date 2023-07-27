from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from .manager import CustomUserManager


# Create your models here.
class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
