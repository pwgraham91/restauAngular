# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restauREST', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='dinner',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='weekday',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
