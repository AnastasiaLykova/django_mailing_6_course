from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Clients(models.Model):
    email = models.EmailField(max_length=100, verbose_name='почта', unique=True)
    fullname = models.CharField(max_length=100, verbose_name='ФИО')
    annotation = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'{self.fullname} {self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'
        ordering = ('email',)
