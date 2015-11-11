import os
from uuid import uuid4

from django.db import models
from django.utils.translation import ugettext_lazy as _



def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    # get filename
        # set filename as random string
    filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join('images/banners', filename)


class Banner(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100,
        blank=True,
        null=True
    )
    image = models.ImageField(
        _('image'),
        upload_to=upload_to,
        max_length=1000,
    )


    class Meta():
        verbose_name = 'banner'
        verbose_name_plural = 'banners'

    def __str__(self):
        return self.name