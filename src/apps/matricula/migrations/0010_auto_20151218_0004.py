# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0009_auto_20151217_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='matricula',
            field=models.OneToOneField(related_name='matricula_recibo', to='matricula.Matricula'),
        ),
    ]
