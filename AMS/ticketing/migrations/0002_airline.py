# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-04 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('airlineId', models.IntegerField(primary_key=True, serialize=False)),
                ('airlineName', models.CharField(max_length=30)),
                ('code', models.CharField(max_length=10)),
            ],
        ),
    ]
