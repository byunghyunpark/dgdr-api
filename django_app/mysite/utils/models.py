from django.db import models

from django.utils.translation import ugettext as _


class TimeStampedModel(models.Model):
    """
    Abstract model for models that require both creation and modification dates.
    """
    created_date = models.DateTimeField(_('created date'), auto_now_add=True)
    modified_date = models.DateTimeField(_('modified_date'), auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_date']
