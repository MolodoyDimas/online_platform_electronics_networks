from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    '''
    Класс пользователя:
    Имя
    Email
    Пароль
    '''

    username= models.CharField(max_length=100, unique=True, verbose_name='Имя пользователя')
    email = models.EmailField(unique=True, verbose_name='Email')
    password = models.CharField(max_length=30, verbose_name='Пароль')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
