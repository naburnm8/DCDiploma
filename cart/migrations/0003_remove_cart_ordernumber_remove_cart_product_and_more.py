# Generated by Django 5.0.6 on 2024-07-14 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='orderNumber',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='product',
        ),
        migrations.AddField(
            model_name='cart',
            name='address',
            field=models.TextField(default='Россия, Москва, ул. Мира, дом 666'),
        ),
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
