from django.db import models

from clients.models import Clients
from users.models import Users

NULLABLE = {'null': True, 'blank': True}


class Message(models.Model):
    heading = models.CharField(max_length=100, verbose_name='заголовок')
    content = models.TextField(verbose_name='сообщение')
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)

    def __str__(self):
        return f'{self.heading}'

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'
        ordering = ('heading',)


class Mailing(models.Model):

    DAY = 'day'
    WEEK = 'week'
    MONTH = 'month'

    PERIODICITY_CHOICES = [
        ('day', 'Раз в день'),
        ('week', 'Раз в неделю',),
        ('month', 'Раз в месяц',),
    ]

    CREATED = 'created'
    STARTED = 'started'
    FINISHED = 'completed'

    STATUS_CHOICES = (
        ('created', 'создана'),
        ('started', 'запущена'),
        ('completed', 'завершена'),
    )

    datetime = models.TimeField(verbose_name='время рассылки')
    periodicity = models.CharField(verbose_name="Периодичность", choices=PERIODICITY_CHOICES,
                                                   default=1)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='статус рассылки', default='created')
    creator = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name='Создатель', **NULLABLE)
    clients = models.ManyToManyField(Clients, verbose_name='клиенты')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)

    def __str__(self):
        return f'{self.datetime}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('datetime',)


class Logs(models.Model):

    SENT = 'sent'
    FAILED = 'failed'
    PENDING = 'pending'

    STATUS_CHOICES = [
        (SENT, 'Отправлено'),
        (FAILED, 'Не удалось отправить'),
        (PENDING, 'В ожидании')
    ]

    datetime = models.TimeField(auto_now_add=True, verbose_name='дата создвния', **NULLABLE)
    change_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки', **NULLABLE)
    status = models.CharField(max_length=10, verbose_name='статус попытки', choices=STATUS_CHOICES, default=PENDING)
    response = models.TextField(verbose_name='ответ почтового сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return f'{self.datetime}'

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
        ordering = ('datetime',)
