# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0017_auto_20160621_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='extra',
            name='profileimage',
            field=models.ImageField(blank=True, default='https://tagyourit.s3.amazonaws.com/static/icon-user-default.png', null=True, upload_to='profilepics'),
        ),
    ]
