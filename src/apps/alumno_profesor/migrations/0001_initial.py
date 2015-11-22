# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=120, verbose_name=b'Nombres')),
                ('apellidos', models.CharField(max_length=120, verbose_name=b'Apellidos')),
                ('sexo', models.CharField(max_length=120, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('telefono', models.CharField(max_length=12, verbose_name='Tel\xe9fono', blank=True)),
                ('direccion', models.CharField(max_length=120, verbose_name=b'Direcci\xc3\xb3n', blank=True)),
                ('codigo_alumno', models.CharField(max_length=12, verbose_name=b'Codigo CIUNAC', blank=True)),
                ('estado', models.BooleanField(default=True, verbose_name=b'Estado')),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha Registrado')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('constancia_tipo_alumno', models.ImageField(upload_to=b'constancia/', verbose_name=b'Constancia de tipo alumno')),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombres', models.CharField(max_length=120, verbose_name=b'Nombres')),
                ('apellidos', models.CharField(max_length=120, verbose_name=b'Apellidos')),
                ('sexo', models.CharField(max_length=120, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('telefono', models.CharField(max_length=12, verbose_name=b'Tel\xc3\xa9fono', blank=True)),
                ('direccion', models.CharField(max_length=120, verbose_name=b'Direcci\xc3\xb3n')),
                ('codigo_profesor', models.CharField(max_length=12, verbose_name=b'Codigo Profesor', blank=True)),
                ('estado', models.BooleanField(default=True, verbose_name=b'Estado')),
                ('email', models.EmailField(max_length=254, verbose_name=b'Email')),
                ('fecha_agregado', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha Registrado')),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesors',
            },
        ),
        migrations.CreateModel(
            name='TipoAlumno',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=120, verbose_name=b'TIpo Alumno')),
            ],
            options={
                'verbose_name': 'TipoAlumno',
                'verbose_name_plural': 'TipoAlumnos',
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='tipo_alumno',
            field=models.ForeignKey(related_name='tipo_alumno_alumno', to='alumno_profesor.TipoAlumno'),
        ),
    ]
