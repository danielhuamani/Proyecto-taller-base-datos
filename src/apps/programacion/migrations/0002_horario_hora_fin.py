# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('programacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='hora_fin',
            field=models.TimeField(default='12:12:12'),
            preserve_default=False,
        ),
    ]
