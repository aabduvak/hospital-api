# Generated by Django 4.1.7 on 2023-03-04 06:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='marital_status',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='visitrequest',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 4, 9, 27, 5, 802260)),
        ),
    ]