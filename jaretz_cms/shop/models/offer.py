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
	name = models.CharField(
		_('name'),
		max_length=50,
		blank=True,
		null=True
	)

	short_description = models.CharField(
		_('short description'),
		max_length=100,
		blank=True,
		null=True
	)

	price = models.DecimalField(
		_('price'),
		max_digits=8,
		decimal_places=2
	)

	image = models.ImageField(
		_('image'),
		upload_to=upload_to,
		null=True,
		blank=True,
		max_length=1000
	)

	class Meta:
		verbose_name='Offer'

	def __str__(self):
		return self.name

    