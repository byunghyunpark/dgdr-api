from django.db import models
from django.utils.translation import ugettext as _


class Province(models.Model):
    """Region main category."""
    name = models.CharField(verbose_name=_('province name'), max_length=50)
    latitude = models.FloatField(verbose_name=_('latitude'))
    longitude = models.FloatField(verbose_name=_('longitude'))

    class Meta:
        verbose_name = _("Province")
        verbose_name_plural = _("Provinces")

    def __str__(self):
        return self.name


class City(models.Model):
    """Region sub category."""
    province = models.ForeignKey(
        verbose_name=_("province"),
        to=Province, on_delete=models.CASCADE,
    )
    name = models.CharField(verbose_name=_('city name'), max_length=50)
    latitude = models.FloatField(verbose_name=_('latitude'))
    longitude = models.FloatField(verbose_name=_('longitude'))

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.name
