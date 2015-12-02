# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models.banner


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20151202_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='item',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='image',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='name',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='price',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='short_description',
        ),
        migrations.AddField(
            model_name='banner',
            name='image',
            field=models.ImageField(default=None, verbose_name='image', max_length=1000, upload_to=shop.models.banner.upload_to),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='banner',
            name='name',
            field=models.CharField(blank=True, verbose_name='name', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='offer',
            name='item',
            field=models.ForeignKey(related_query_name='item', verbose_name='item offer', related_name='items', blank=True, null=True, to='shop.Item'),
        ),
    ]
