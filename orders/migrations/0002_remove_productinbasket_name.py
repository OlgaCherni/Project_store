# Generated by Django 5.0.2 on 2024-06-05 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinbasket',
            name='name',
        ),
    ]