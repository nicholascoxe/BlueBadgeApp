# Generated by Django 2.1.7 on 2019-03-14 20:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20190313_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 20, 40, 12, 721943, tzinfo=utc)),
        ),
    ]
