from django.db import models
from django.utils.translation import ugettext_lazy as _


class Shop(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100
    )
    slogan = models.CharField(
        _('slogan'),
        max_length=150,
        blank=True,
        null=True
    )
    address = models.CharField(
        _('address'),
        max_length=75,
        blank=True,
        null=True
    )
    city = models.CharField(
        _('city'),
        max_length=20,
        blank=True,
        null=True
    )
    town_ship = models.CharField(
        _('town ship'),
        max_length=20,
        blank=True,
        null=True
    )
    zip_code = models.CharField(
        _('zip code'),
        max_length=10,
        blank=True,
        null=True
    )
    country = models.CharField(
        _('country'),
        max_length=20,
        blank=True,
        null=True
    )
    tax_number = models.CharField(
        _('utr'),
        max_length=20
    )
    phone = models.CharField(
        _('phone'),
        max_length=15,
        blank=True,
        null=True
    )
    email = models.EmailField(
        _('email'),
        blank=True,
        null=True
    )
    terms_use_privacy = fields.RedactorField(
        _('terms of use and privacy'),
        blank=True,
        null=True
    )
    return_policy = fields.RedactorField(
        _('return policy'),
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('shop information')

    def __str__(self):
        return self.name
