# Generated by Django 4.2 on 2023-04-15 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitrequest',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 15, 22, 34, 28, 105445)),
        ),
    ]