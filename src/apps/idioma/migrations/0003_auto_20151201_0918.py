# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idioma', '0002_cicloidioma_idioma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cicloidioma',
            name='nombre',
            field=models.CharField(max_length=120, verbose_name=b'Nombre'),
        ),
    ]
