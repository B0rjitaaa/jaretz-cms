# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20151130_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(related_query_name='parent', to='shop.Category', null=True, verbose_name='parent category', blank=True, related_name='parent'),
        ),
    ]
