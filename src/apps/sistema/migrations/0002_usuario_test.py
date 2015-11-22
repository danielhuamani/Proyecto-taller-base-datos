# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='test',
            field=models.CharField(default='', max_length=120, verbose_name=b'Test'),
            preserve_default=False,
        ),
    ]
