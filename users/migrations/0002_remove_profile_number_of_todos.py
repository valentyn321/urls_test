# Generated by Django 3.0.5 on 2020-04-09 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='number_of_todos',
        ),
    ]
