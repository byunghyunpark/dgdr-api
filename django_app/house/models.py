from django.db import models
from django.utils.translation import ugettext_lazy as _
from geoposition.fields import GeopositionField
from smart_selects.db_fields import ChainedForeignKey

from mysite.utils.models import TimeStampedModel
from region.models import Province, City


class SearchTag(models.Model):
    """House's search tag."""
    name = models.CharField(verbose_name=_("name"), max_length=30)

    class Meta:
        verbose_name = _("Search tag")
        verbose_name_plural = _("Search tags")

    def __str__(self):
        return self.name


class House(TimeStampedModel):
    """Share house's key information."""
    name = models.CharField(verbose_name=_("name"), max_length=30)
    main_photo = models.ImageField(verbose_name=_("main photo"), upload_to="house_main_photo")
    introduction = models.TextField(verbose_name=_("introduction"), blank=True, null=True)
    trading_area = models.CharField(verbose_name=_("trading area"), max_length=50)
    opened_date = models.DateField(verbose_name=_("opened date"))
    capacity = models.IntegerField(verbose_name=_("capacity"))
    category = models.CharField(verbose_name=_("category"), max_length=30)

    province = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)
    city = ChainedForeignKey(
        verbose_name=_("city"),
        to=City,
        chained_field='province',
        chained_model_field='province',
        show_all=False, auto_choose=True, sort=True,
        null=True,
    )
    address = models.CharField(verbose_name=_('address'), max_length=100, null=True)
    position = GeopositionField(verbose_name=_('position'))

    common_service = models.TextField(verbose_name=_("common service"), blank=True, null=True)
    private_service = models.TextField(verbose_name=_("private service"), blank=True, null=True)
    transportation = models.TextField(verbose_name=_("transportation"), blank=True, null=True)
    accessibility = models.TextField(verbose_name=_("accessibility"), blank=True, null=True)
    amenity = models.TextField(verbose_name=_("amenity"), blank=True, null=True)

    search_tag = models.ManyToManyField(verbose_name=_("tag"), to=SearchTag, blank=True)
    sort_score = models.IntegerField(verbose_name=_("sort score"), default=0)
    STATUS = (
        ("open", _("open")),
        ("close", _("close")),
        ("Ready", _("ready")),
    )
    status = models.CharField(verbose_name=_("status"), max_length=30, choices=STATUS, default="ready")

    class Meta:
        ordering = ("sort_score", )
        verbose_name = _("House")
        verbose_name_plural = _("Houses")

    def __str__(self):
        return self.name
