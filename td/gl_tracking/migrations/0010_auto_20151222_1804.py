# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 18:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gl_tracking', '0009_auto_20151222_1754'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='progress',
            unique_together=set([('language', 'type')]),
        ),
    ]
