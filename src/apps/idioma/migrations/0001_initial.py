# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CicloIdioma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=2, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name': 'CicloIdioma',
                'verbose_name_plural': 'CicloIdiomas',
            },
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, verbose_name=b'Nombre del idioma')),
            ],
            options={
                'verbose_name': 'Idioma',
                'verbose_name_plural': 'Idiomas',
            },
        ),
        migrations.CreateModel(
            name='NivelIdioma',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, verbose_name=b'Nombre del Nivel idioma', choices=[(b'B', b'Basico'), (b'I', b'Intermedio'), (b'A', b'Avanzado')])),
            ],
            options={
                'verbose_name': 'Nivel Idioma',
                'verbose_name_plural': 'Nivel Idiomas',
            },
        ),
        migrations.AddField(
            model_name='cicloidioma',
            name='nivel_idioma',
            field=models.ForeignKey(related_name='nivel_idioma_ciclo', to='idioma.NivelIdioma'),
        ),
    ]
