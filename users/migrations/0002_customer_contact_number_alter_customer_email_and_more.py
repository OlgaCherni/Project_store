# Generated by Django 5.0.2 on 2024-06-05 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='contact_number',
            field=models.CharField(default='+375447756610', max_length=50),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=40, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='second_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
    ]
