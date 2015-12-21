# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0006_auto_20151220_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name=b'\xc3\x9altimo Login', blank=True),
        ),
    ]
