# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0003_auto_20151215_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='alumno',
            field=models.ForeignKey(related_name='alumno_matricula', blank=True, to='alumno_profesor.Alumno', null=True),
        ),
    ]
