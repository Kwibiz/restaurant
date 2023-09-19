from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adress = models.CharField(max_length=80)
    is_vegetarian = models.BooleanField(default=False)
    has_reservation = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class  Establishment(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=80)
    has_vegetarian_dishes = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    

class Tables(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    table_is_reserved = models.BooleanField(default=False)
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    reservation_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Tables"

    def __str__(self) -> str:
        return str(self.table_number)

class Dish(models.Model):
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    ingredients = models.TextField(blank=True)
    description = models.TextField(blank=True)
    is_vegetarian = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    table = models.OneToOneField(Tables, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.dish} for table №{self.table}'


class Reservation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    establishment = models.ForeignKey(Establishment, on_delete=models.CASCADE, null=True)
    table = models.OneToOneField(Tables, on_delete=models.CASCADE, null=True)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, null=True)
    time = models.DateTimeField(null=True)
