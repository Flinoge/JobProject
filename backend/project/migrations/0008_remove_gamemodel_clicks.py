# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-07 22:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_auto_20170807_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemodel',
            name='clicks',
        ),
    ]
