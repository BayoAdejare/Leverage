# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-21 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaignfinance',
            name='Date',
            field=models.DateField(),
        ),
    ]