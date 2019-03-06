# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-25 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantInactivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_tenant', models.IntegerField(blank=True, null=True)),
                ('url', models.CharField(default='', max_length=200, null=True)),
            ],
            options={
                'db_table': 'TenantInactivo',
            },
        ),
    ]