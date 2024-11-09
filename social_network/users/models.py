from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class Users(AbstractBaseUser):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=40)
    e_mail = models.CharField(max_length=20, blank=True, unique=True)
    wallet_address = models.CharField(blank=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password"]
