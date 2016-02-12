# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-25 19:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('td', '0010_remove_region_wa_director'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gl_tracking', '0021_auto_20160125_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='GLDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('regions', models.ManyToManyField(blank=True, to='td.Region')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]