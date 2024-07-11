from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    user_address = models.TextField(null=True, blank=True)
