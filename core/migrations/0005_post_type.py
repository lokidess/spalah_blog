# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-03 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180903_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.IntegerField(choices=[(0, 'News'), (1, 'Story'), (2, 'Art')], null=True),
        ),
    ]
