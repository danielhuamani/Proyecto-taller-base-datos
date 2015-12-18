# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0008_recibo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='numero_recibo',
            field=models.IntegerField(unique=True, verbose_name=b'Numero de Recibo'),
        ),
    ]
