# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 20:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gl_tracking', '0018_auto_20160121_1948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='method',
            old_name='code',
            new_name='slug',
        ),
    ]
