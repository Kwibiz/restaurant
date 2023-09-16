from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adress = models.CharField(max_length=80)
    is_vegetarian = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)