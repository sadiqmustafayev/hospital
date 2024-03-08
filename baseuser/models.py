from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


class BaseUser(AbstractUser):
  location = models.CharField(max_length=50)
  updated_at = models.DateTimeField(auto_now=True)
  date_of_birth = models.DateField(blank=True, null=True)
  phone_number = PhoneNumberField(blank=True)
  email = models.EmailField(max_length=255, unique=True)
