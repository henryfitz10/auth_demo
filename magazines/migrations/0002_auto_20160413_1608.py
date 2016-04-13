# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazine',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images', blank=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='subscription_end',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 13, 15, 8, 9, 133000, tzinfo=utc)),
        ),
    ]
