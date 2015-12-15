# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0003_auto_20151213_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aula',
            name='numero_aula',
            field=models.IntegerField(unique=True, verbose_name=b'Numero de aula'),
        ),
    ]
