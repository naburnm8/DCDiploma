from django.db import models


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
