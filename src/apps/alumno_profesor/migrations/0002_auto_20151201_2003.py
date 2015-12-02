# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='telefono',
            field=models.CharField(max_length=12, verbose_name=b'Tel\xc3\xa9fono', blank=True),
        ),
    ]
