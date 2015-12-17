# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0005_matricula_observacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='matricula',
            name='estado',
            field=models.BooleanField(default=False, verbose_name=b'Estado'),
        ),
    ]
