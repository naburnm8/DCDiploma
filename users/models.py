from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_address = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(unique=True)
