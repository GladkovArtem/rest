from django.db import models
from uuid import uuid4


class Author(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(blank=True, verbose_name='Email', unique=True)
    user_name = models.CharField(max_length=64, default=email, verbose_name='Пользователь', unique=True)
    # birthday_year = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
