from django.db import models

from users.models import User


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    count = models.IntegerField()
    category = models.ForeignKey(
        Category,
        related_name='products',
        on_delete=models.CASCADE
    )
    shop = models.ForeignKey(
        Shop,
        related_name='products',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'{self.user} {self.product} {self.quantity}'

    def sum(self):
        return self.quantity * self.product.price
