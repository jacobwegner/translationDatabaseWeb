# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20150902_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charter',
            name='lead_dept',
        ),
        migrations.AddField(
            model_name='charter',
            name='lead_dept',
            field=models.ForeignKey(verbose_name=b'Lead Department', to='tracking.Department', null=True),
        ),
    ]
