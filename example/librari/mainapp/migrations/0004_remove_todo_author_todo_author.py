# Generated by Django 4.1.5 on 2023-01-15 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_project_todo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='author',
        ),
        migrations.AddField(
            model_name='todo',
            name='author',
            field=models.ManyToManyField(to='mainapp.author'),
        ),
    ]
