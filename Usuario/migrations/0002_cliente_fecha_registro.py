# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-16 15:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='fecha_registro',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2017, 5, 16, 15, 23, 11, 878084, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
