# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0004_auto_20151215_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='nombres',
            field=models.CharField(max_length=120, verbose_name=b'Nombres'),
        ),
    ]
