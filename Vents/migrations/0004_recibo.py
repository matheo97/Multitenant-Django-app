# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-24 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vents', '0003_auto_20170522_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc', models.FileField(blank=True, null=True, upload_to='recibo/')),
            ],
        ),
    ]
