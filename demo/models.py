from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

# Create your models here.


class User(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    is_deleted = models.BooleanField(_('is_deleted'), default=False, help_text=_(
        'Designates whether this user should be treated as delete user. '), )
    mobile_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=140, null=True, blank=True)
    state = models.CharField(max_length=140, null=True, blank=True)
    zip_code = models.CharField(max_length=140, null=True, blank=True)
    date_of_birth = models.DateField(_('date of birth'), null=True, blank=True)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default='O')
    profile_pic = models.ImageField(upload_to='images', null=True, blank=True)
    hobbies = models.TextField(null=True, blank=True)

    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
