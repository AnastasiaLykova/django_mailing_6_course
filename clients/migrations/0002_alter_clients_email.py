# Generated by Django 4.2.5 on 2023-09-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='почта'),
        ),
    ]
