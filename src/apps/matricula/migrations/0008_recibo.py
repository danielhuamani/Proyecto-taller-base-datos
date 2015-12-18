# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0007_matricula_fecha_creacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recibo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha creacion')),
                ('numero_recibo', models.IntegerField(verbose_name=b'Numero de Recibo')),
                ('matricula', models.ForeignKey(related_name='matricula_recibo', to='matricula.Matricula')),
            ],
            options={
                'verbose_name': 'Recibo',
                'verbose_name_plural': 'Recibos',
            },
        ),
    ]
