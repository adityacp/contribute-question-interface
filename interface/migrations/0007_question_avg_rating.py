# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-23 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0006_auto_20160621_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='avg_rating',
            field=models.IntegerField(default=0),
        ),
    ]