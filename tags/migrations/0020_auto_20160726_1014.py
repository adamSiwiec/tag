# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0019_auto_20160726_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='profileimage',
            field=models.ImageField(blank=True, default='https://tagyourit.s3.amazonaws.com/static/icon-user-default.png', null=True, upload_to='profilepics'),
        ),
    ]