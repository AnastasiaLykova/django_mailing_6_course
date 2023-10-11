# Generated by Django 4.2.5 on 2023-10-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0004_message_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='status',
            field=models.CharField(choices=[('created', 'создана'), ('started', 'запущена'), ('completed', 'завершена')], default='created', max_length=10, verbose_name='статус рассылки'),
        ),
    ]