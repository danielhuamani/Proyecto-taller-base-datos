# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.BooleanField(default=True, verbose_name=b'\xc2\xbfActivo?')),
                ('last_login', models.DateTimeField(null=True, verbose_name=b'\xc3\x9altimo Login', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email', blank=True)),
                ('password', models.CharField(default=b'', max_length=255, verbose_name=b'Contrase\xc3\xb1a', blank=True)),
                ('set_password', models.BooleanField(default=False, verbose_name=b'\xc2\xbfContrase\xc3\xb1a encriptada?')),
                ('uuid_hash', models.CharField(default=b'', help_text=b'Aleautorio utilizado para recuperar la contrase\xc3\xb1a', max_length=36, verbose_name=b'UUID', blank=True)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            bases=(models.Model,),
        ),
    ]
