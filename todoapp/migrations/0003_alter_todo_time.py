# Generated by Django 3.2.3 on 2021-05-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todo_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
