# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import shop.models.item
import django.core.validators
from decimal import Decimal
import shop.models.banner
import shop.models.category


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(null=True, blank=True, max_length=100, verbose_name='name')),
                ('image', models.ImageField(upload_to=shop.models.banner.upload_to, max_length=1000, verbose_name='image')),
            ],
            options={
                'verbose_name_plural': 'banners',
                'verbose_name': 'banner',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('slug', models.SlugField(null=True, blank=True, max_length=100)),
                ('header_image', models.ImageField(null=True, blank=True, max_length=1000, verbose_name='header image', upload_to=shop.models.category.upload_to)),
                ('thumbnail', models.ImageField(null=True, blank=True, max_length=1000, verbose_name='miniature image', upload_to=shop.models.category.upload_to)),
                ('meta_tag', models.CharField(null=True, blank=True, max_length=500, verbose_name='meta tag')),
            ],
            options={
                'verbose_name_plural': 'categories',
                'verbose_name': 'category',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('reference_code', models.CharField(max_length=100, verbose_name='reference_code')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('starred', models.BooleanField(default=False, verbose_name='starred')),
                ('visible', models.BooleanField(default=True, verbose_name='visible')),
                ('wholesale_price', models.DecimalField(max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='wholesale price')),
                ('price', models.DecimalField(max_digits=8, decimal_places=2, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='price')),
                ('upload_date', models.DateField(verbose_name='date added', auto_now_add=True)),
                ('times_sold', models.PositiveIntegerField(default=0, verbose_name='times sold')),
                ('shown_times', models.PositiveIntegerField(default=0, verbose_name='shown times')),
                ('slug', models.SlugField(null=True, blank=True, max_length=100)),
                ('image', models.ImageField(null=True, blank=True, max_length=1000, upload_to=shop.models.item.upload_to)),
                ('category', models.ForeignKey(related_name='items', null=True, related_query_name='item', to='shop.Category', blank=True, verbose_name='category')),
            ],
            options={
                'verbose_name_plural': 'Items',
                'verbose_name': 'Item',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slogan', models.CharField(null=True, blank=True, max_length=150, verbose_name='slogan')),
                ('address', models.CharField(null=True, blank=True, max_length=75, verbose_name='address')),
                ('city', models.CharField(null=True, blank=True, max_length=20, verbose_name='city')),
                ('town_ship', models.CharField(null=True, blank=True, max_length=20, verbose_name='town ship')),
                ('zip_code', models.CharField(null=True, blank=True, max_length=10, verbose_name='zip code')),
                ('country', models.CharField(null=True, blank=True, max_length=20, verbose_name='country')),
                ('tax_number', models.CharField(max_length=20, verbose_name='utr')),
                ('phone', models.CharField(null=True, blank=True, max_length=15, verbose_name='phone')),
                ('email', models.EmailField(null=True, blank=True, max_length=75, verbose_name='email')),
                ('terms_use_privacy', models.TextField(null=True, blank=True, verbose_name='terms of use and privacy')),
                ('return_policy', models.TextField(null=True, blank=True, verbose_name='return policy')),
            ],
            options={
                'verbose_name': 'shop information',
            },
            bases=(models.Model,),
        ),
    ]
