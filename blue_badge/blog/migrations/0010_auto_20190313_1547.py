# Generated by Django 2.1.7 on 2019-03-13 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190313_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 13, 15, 47, 56, 295240, tzinfo=utc)),
        ),
    ]