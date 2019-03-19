# Generated by Django 2.1.7 on 2019-03-19 19:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20190319_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpeg', upload_to='post_pics'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 19, 19, 43, 6, 469853, tzinfo=utc)),
        ),
    ]