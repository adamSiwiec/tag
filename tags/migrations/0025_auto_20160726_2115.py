# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0024_auto_20160726_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='profileimage',
            field=models.ImageField(blank=True, upload_to='profilepics/'),
        ),
    ]
