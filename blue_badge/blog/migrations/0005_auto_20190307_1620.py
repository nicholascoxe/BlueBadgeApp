# Generated by Django 2.1.7 on 2019-03-07 16:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190306_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 7, 16, 20, 19, 850207, tzinfo=utc)),
        ),
    ]
