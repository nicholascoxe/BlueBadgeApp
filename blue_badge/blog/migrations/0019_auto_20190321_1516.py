# Generated by Django 2.1.7 on 2019-03-21 15:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190320_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 21, 15, 16, 57, 706309, tzinfo=utc)),
        ),
    ]
