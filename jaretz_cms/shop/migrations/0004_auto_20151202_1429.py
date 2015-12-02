# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='image',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='name',
        ),
        migrations.AddField(
            model_name='banner',
            name='item',
            field=models.ForeignKey(related_query_name='item', related_name='items', verbose_name='item banner', to='shop.Item', blank=True, null=True),
        ),
    ]
