# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('idioma', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cicloidioma',
            name='idioma',
            field=models.ForeignKey(related_name='idioma_ciclo_idioma', default='', to='idioma.Idioma'),
            preserve_default=False,
        ),
    ]
