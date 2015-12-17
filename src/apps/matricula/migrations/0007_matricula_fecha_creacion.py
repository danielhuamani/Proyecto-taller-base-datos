# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0006_matricula_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='fecha_creacion',
            field=models.DateTimeField(default='2000-12-12 11:11:00', verbose_name=b'fecha_creacion', auto_now_add=True),
            preserve_default=False,
        ),
    ]
