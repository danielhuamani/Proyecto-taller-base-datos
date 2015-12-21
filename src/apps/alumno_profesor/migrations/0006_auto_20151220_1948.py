# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0005_auto_20151217_1616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='alumno',
            old_name='estado',
            new_name='is_active',
        ),
    ]
