# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0009_extra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra',
            name='profileimage',
            field=models.ImageField(default='icon-user-default.svg', upload_to='images'),
        ),
    ]
