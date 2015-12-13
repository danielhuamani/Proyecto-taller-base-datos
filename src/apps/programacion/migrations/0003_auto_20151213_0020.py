# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumno_profesor', '0003_auto_20151207_1628'),
        ('idioma', '0005_remove_idioma_test'),
        ('programacion', '0002_horario_hora_fin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aula', models.ForeignKey(related_name='aula_programacion', to='programacion.Aula')),
                ('ciclo_idioma', models.ForeignKey(related_name='ciclo_idioma_programacion', to='idioma.CicloIdioma')),
            ],
            options={
                'verbose_name': 'Programacion',
                'verbose_name_plural': 'Programacions',
            },
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora',
            field=models.TimeField(verbose_name=b'Horario Inicio'),
        ),
        migrations.AlterField(
            model_name='horario',
            name='hora_fin',
            field=models.TimeField(verbose_name=b'Horario FIn'),
        ),
        migrations.AddField(
            model_name='programacion',
            name='horario',
            field=models.ForeignKey(related_name='horario_programacion', to='programacion.Horario'),
        ),
        migrations.AddField(
            model_name='programacion',
            name='periodo',
            field=models.ForeignKey(related_name='periodo_programacion', to='programacion.Periodo'),
        ),
        migrations.AddField(
            model_name='programacion',
            name='profesor',
            field=models.ForeignKey(related_name='profesor_programacion', to='alumno_profesor.Profesor'),
        ),
    ]
