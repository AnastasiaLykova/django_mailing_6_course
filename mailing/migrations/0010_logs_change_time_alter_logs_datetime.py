# Generated by Django 4.2.5 on 2023-10-21 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0009_alter_mailing_clients'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='change_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='дата и время последней попытки'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='datetime',
            field=models.TimeField(auto_now_add=True, null=True, verbose_name='дата создвния'),
        ),
    ]
