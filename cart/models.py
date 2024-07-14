from users.models import User
from django.db import models

from products.models import Product


class Cart(models.Model):
    STATUS_CHOICES = [(0, "Создаётся"), (1, "Оплачен"), (2, "Доставлен")]
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=0)
    date = models.DateField().auto_now
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket_history = models.JSONField(default=dict)
    address = models.TextField(default='Россия, Москва, ул. Мира, дом 666')

    def __str__(self):
        return f'Order #{self.id}'
