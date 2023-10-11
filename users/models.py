from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Users(AbstractUser):

    username = None

    email = models.EmailField(max_length=100, verbose_name='почта', unique=True)
    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=35, verbose_name='страна', **NULLABLE)

    verify_key = models.CharField(max_length=35, verbose_name='ключ верификации', **NULLABLE)
    is_verified = models.BooleanField(default=False, verbose_name='верификация по почте')
    is_active = models.BooleanField(default=True, verbose_name='признак активности')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
