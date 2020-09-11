import json

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _

from six import python_2_unicode_compatible@python_unicode_compatible



class Author(models.model):
    """Author."""

    salutation = models.CharField(max_length=10)
    name = models.CharField(max_lengh=200)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='authors', null=True, blank=true

    class Meta(object):
    """Meta Options."""
        ordering = ["id"]

    def __str__(self):
        return self.name

