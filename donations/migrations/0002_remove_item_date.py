# Generated by Django 3.0.4 on 2021-01-12 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='date',
        ),
    ]
