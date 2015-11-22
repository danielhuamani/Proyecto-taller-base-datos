# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0002_usuario_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='test',
        ),
    ]
