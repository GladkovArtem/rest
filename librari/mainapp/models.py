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


class Project(models.Model):
    project_name = models.CharField(max_length=64, verbose_name='Название проекта', unique=True)
    link = models.CharField(max_length=512, verbose_name='Ссылка на репозиорий')
    authors = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class TODO(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.CharField(max_length=512, verbose_name='Текст')
    create_date = models.DateTimeField(verbose_name='Дата создания')
    update_date = models.DateTimeField(verbose_name='Дата обновления')
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    is_active = models.BooleanField(verbose_name='Статус активности')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
