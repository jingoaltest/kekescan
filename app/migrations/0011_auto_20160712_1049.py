# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-12 02:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160712_1040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burp',
            name='queryed',
        ),
        migrations.AlterField(
            model_name='burp',
            name='isComplete',
            field=models.IntegerField(max_length=1, verbose_name=b'isComplete'),
        ),
        migrations.AlterField(
            model_name='icpcheck',
            name='insert_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 10, 49, 0, 312335), null=True),
        ),
        migrations.AlterField(
            model_name='subdomainbrute',
            name='fuzz_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 7, 12, 10, 49, 0, 312888), null=True),
        ),
    ]
