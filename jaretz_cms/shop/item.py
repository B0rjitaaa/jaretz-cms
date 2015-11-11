from hashlib import sha1
import os
from uuid import uuid4

from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _

def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
        # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join('images/items', filename)

class Item(models.Model):
	reference_code = models.CharField(
        _('reference code'),
        max_length=100
    )
	name = models.CharField(
		_('name'),
		max_length=150
	)
	detailed_description = models.TextField(
        _('detailed description'),
        null=True,
        blank=True
    )
    short_description = models.TextField(
        _('short description'),
        null=True,
        blank=True
    )
    starred = models.BooleanField(
        _('starred'),
        default=False
    )
    visible = models.BooleanField(
        _('visible'),
        default=True
    )
    wholesale_price = models.DecimalField(
        _('wholesale price'),
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    price = models.DecimalField(
        _('price'),
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    upload_date = models.DateField(
        _('date added'),
        auto_now_add=True
    )
    times_sold = models.PositiveIntegerField(
        _('times sold'),
        default=0
    )
    shown_times = models.PositiveIntegerField(
        _('shown times'),
        default=0
    )
    slug = models.SlugField(
        max_length=100,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'Category',
        related_name='items',
        related_query_name='item',
        verbose_name=_('category'),
        blank=True,
        null=True
    )
    image = models.ImageField(
      upload_to=upload_to,
      null=True,
      blank=True,
      max_length=1000
    )
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Item, self).save(*args, **kwargs)