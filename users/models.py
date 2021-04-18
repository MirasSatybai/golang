from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=32, unique=True)
    phone_number = models.CharField(max_length=12)
    password = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    avatar = models.TextField(default="default_avatar.png")
