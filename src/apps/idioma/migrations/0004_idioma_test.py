# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idioma', '0003_auto_20151201_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='idioma',
            name='test',
            field=models.CharField(default='', max_length=120, verbose_name=b'test'),
            preserve_default=False,
        ),
    ]
