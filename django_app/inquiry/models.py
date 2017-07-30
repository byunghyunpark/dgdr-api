import re

from django.db import models
from django.utils.translation import ugettext_lazy as _
from smart_selects.db_fields import ChainedForeignKey

from house.models import House, Room
from mysite.utils.models import TimeStampedModel


class PartnerInquiry(TimeStampedModel):
    name = models.CharField(verbose_name=_("name"), max_length=20)
    phone_number = models.CharField(verbose_name=_("phone number"), max_length=20)
    email = models.EmailField(verbose_name=_("email"), max_length=100, blank=True, null=True)
    address = models.CharField(verbose_name=_('address'), max_length=100)
    memo = models.TextField(verbose_name=_("memo"), blank=True, null=True)
    STATUS = (
        ("progress", _("progress")),
        ("complete", _("complete")),
        ("cancel", _("cancel")),
    )
    status = models.CharField(verbose_name=_("status"), choices=STATUS, max_length=20)
    inquiry_route = models.CharField(verbose_name=_("inquiry route"), max_length=30, blank=True, null=True)

    class Meta:
        verbose_name = _("Partner inquiry")
        verbose_name_plural = _("Partner inquiries")

    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        # Phone number validation
        self.user_phone_number = re.sub(r'[^0-9]', r'', str(self.phone_number))
        super(PartnerInquiry, self).save(*arg, **kwargs)


class TenantInquiry(TimeStampedModel):
    name = models.CharField(verbose_name=_("name"), max_length=20)
    SEX = (
        ("man", _("man")),
        ("woman", _("woman")),
    )
    sex = models.CharField(verbose_name=_("sex"), choices=SEX, max_length=20)
    phone_number = models.CharField(verbose_name=_("phone number"), max_length=20)
    email = models.EmailField(verbose_name=_("email"), max_length=100, blank=True, null=True)
    house = models.ForeignKey(verbose_name=_("house"), to=House)
    room = ChainedForeignKey(
        verbose_name=_("room"),
        to=Room,
        chained_field='house', chained_model_field='house',
        show_all=False, auto_choose=True, sort=True,
        null=True,
    )
    moving_date = models.DateField(verbose_name=_("moving date"))
    memo = models.TextField(verbose_name=_("memo"), blank=True, null=True)
    is_tenant = models.BooleanField(verbose_name=_("is tenant"), default=False)

    class Meta:
        verbose_name = _("Tenant inquiry")
        verbose_name_plural = _("Tenant inquiries")

    def __str__(self):
        return self.name

    def save(self, *arg, **kwargs):
        # Phone number validation
        self.user_phone_number = re.sub(r'[^0-9]', r'', str(self.phone_number))
        super(TenantInquiry, self).save(*arg, **kwargs)
