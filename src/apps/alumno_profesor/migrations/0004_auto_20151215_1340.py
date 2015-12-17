# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0003_auto_20151207_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='contrasena',
            field=models.CharField(default='', max_length=60, verbose_name=b'Contrase\xc3\xb1a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombres',
            field=models.CharField(max_length=120, verbose_name=b'Nombres y Apellidos'),
        ),
    ]
