# Generated by Django 3.2.8 on 2021-10-09 23:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='crud',
            name='update_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
