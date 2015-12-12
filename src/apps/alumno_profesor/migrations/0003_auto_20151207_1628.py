# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0002_auto_20151201_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='codigo_profesor',
            field=models.CharField(unique=True, max_length=12, verbose_name=b'Codigo Profesor', blank=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='email',
            field=models.EmailField(unique=True, max_length=254, verbose_name=b'Email'),
        ),
    ]
