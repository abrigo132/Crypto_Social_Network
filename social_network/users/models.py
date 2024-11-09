from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=40)
    e_mail = models.CharField(max_length=20, blank=True)
    wallet_address = models.CharField(blank=True)
