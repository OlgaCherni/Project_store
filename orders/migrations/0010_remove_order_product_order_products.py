# Generated by Django 5.0.2 on 2024-06-15 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(blank=True, to='orders.productinbasket'),
        ),
    ]
