# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20151202_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='email',
            field=models.EmailField(blank=True, verbose_name='email', max_length=75, null=True),
            preserve_default=True,
        ),
    ]
