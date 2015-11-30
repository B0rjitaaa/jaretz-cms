# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shop.models.offer


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='name', null=True)),
                ('short_description', models.CharField(blank=True, max_length=100, verbose_name='short description', null=True)),
                ('price', models.DecimalField(verbose_name='price', max_digits=8, decimal_places=2)),
                ('image', models.ImageField(blank=True, max_length=1000, verbose_name='image', upload_to=shop.models.offer.upload_to, null=True)),
            ],
            options={
                'verbose_name': 'Offer',
            },
        ),
        migrations.AlterField(
            model_name='shop',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email', null=True),
        ),
    ]
