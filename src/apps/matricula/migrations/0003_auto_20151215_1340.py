# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0002_auto_20151215_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='recibo',
            field=models.FileField(upload_to=b'recibo', verbose_name=b'Recibo de la matricula'),
        ),
    ]
