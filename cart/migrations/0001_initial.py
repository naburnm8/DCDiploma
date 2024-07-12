# Generated by Django 5.0.6 on 2024-07-12 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[(0, 'Создаётся'), (1, 'Оплачен'), (2, 'Доставлен')], default=0, max_length=50)),
                ('date', models.DateField()),
                ('quantity', models.PositiveIntegerField()),
                ('orderNumber', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
