# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0003_auto_20151207_1628'),
        ('programacion', '0004_auto_20151215_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recibo', models.FileField(upload_to=b'recibo', verbose_name=b'Recibo')),
                ('alumno', models.ForeignKey(related_name='alumno_matricula', to='alumno_profesor.Alumno')),
                ('programacion', models.ForeignKey(related_name='programacion_matricula', to='programacion.Programacion')),
            ],
            options={
                'verbose_name': 'Matricula',
                'verbose_name_plural': 'Matriculas',
            },
        ),
    ]
