from hashlib import sha1
import os
from uuid import uuid4
from decimal import Decimal, ROUND_HALF_UP

from django.core.validators import MinValueValidator
from django.core.validators import RegexValidator

from django.template import defaultfilters

from django.db import models

from django.utils.translation import ugettext_lazy as _


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
        # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join('images/offers', filename)


class Offer(models.Model):
	item = models.ForeignKey(
        'Item',
        related_name='items',
        related_query_name='item',
        verbose_name=_('item offer'),
        blank=True,
        null=True
    )
	class Meta:
		verbose_name='Offer'

	def __str__(self):
		return self.item.name

    