from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Cart(models.Model):
    STATUS_CHOICES = [(0, "Создаётся"), (1, "Оплачен"), (2, "Доставлен")]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=0)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.date


