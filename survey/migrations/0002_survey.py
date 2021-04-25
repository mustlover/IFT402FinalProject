# Generated by Django 3.0.4 on 2021-04-10 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_one', models.CharField(max_length=30, null=True)),
                ('option_two', models.CharField(max_length=30, null=True)),
                ('option_three', models.CharField(max_length=30, null=True)),
                ('option_four', models.CharField(max_length=30, null=True)),
                ('option_one_count', models.IntegerField(default=0)),
                ('option_two_count', models.IntegerField(default=0)),
                ('option_three_count', models.IntegerField(default=0)),
                ('option_four_count', models.IntegerField(default=0)),
                ('textAnswer', models.TextField()),
            ],
        ),
    ]