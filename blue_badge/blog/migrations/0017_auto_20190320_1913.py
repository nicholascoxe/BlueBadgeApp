# Generated by Django 2.1.7 on 2019-03-20 19:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20190320_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 20, 19, 13, 22, 711610, tzinfo=utc)),
        ),
    ]