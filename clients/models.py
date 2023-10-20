from django.db import models

from users.models import Users

NULLABLE = {'null': True, 'blank': True}


class Clients(models.Model):

    email = models.EmailField(max_length=100, verbose_name='почта', unique=True)
    fullname = models.CharField(max_length=100, verbose_name='ФИО', **NULLABLE)
    annotation = models.TextField(verbose_name='комментарий', **NULLABLE)
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('fullname',)
