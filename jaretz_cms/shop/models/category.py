import os
from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.template import defaultfilters
from django.conf import settings


def upload_to(instance, filename):
    # get filename
    ext = filename.split('.')[-1]
    # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join('images/categories', filename)


class Category(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100
    )
    description = models.TextField(
        _('description')
    )
    slug = models.SlugField(
        max_length=100,
        null=True,
        blank=True
    )
    header_image = models.ImageField(
        _('header image'),
        upload_to=upload_to,
        max_length=1000,
        null=True,
        blank=True
    )
    thumbnail = models.ImageField(
        _('miniature image'),
        upload_to=upload_to,
        max_length=1000,
        null=True,
        blank=True
  )
    meta_tag = models.CharField(
        _('meta tag'),
        max_length=500,
        null=True,
        blank=True
    )


    @property
    def thumbnail_or_default(self):
        if self.thumbnail:
            return self.thumbnail
        else:
            for i in self.items:
                if i.main_image.path:
                    return i.main_image
        return None

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Category, self).save(*args, **kwargs)
