from django.db import models
from django.utils.translation import ugettext_lazy as _


class News(models.Model):
    """Main page news"""
    title = models.CharField(verbose_name=_("title"), max_length=100)
    context = models.TextField(verbose_name=_("context"))
    photo = models.ImageField(verbose_name=_("photo"), upload_to="news_photo")
    link_url = models.URLField(verbose_name=_("link url"))
    my_order = models.PositiveIntegerField(verbose_name=_("my_order"), default=0, blank=False, null=False)

    class Meta:
        ordering = ['my_order', ]
        verbose_name = _("MainNews")
        verbose_name_plural = _("MainNewses")


class TopBanner(models.Model):
    """Main page top banner"""
    text = models.TextField(verbose_name=_("text"))
    is_active = models.BooleanField(verbose_name=_("is active"), default=True)

    class Meta:
        verbose_name = _("TopBanner")
        verbose_name_plural = _("TopBanners")


class TenantFAQ(models.Model):
    """Main page Tenant FAQ"""
    question = models.CharField(verbose_name=_("question"), max_length=50)
    answer = models.CharField(verbose_name=_("answer"), max_length=50)
    my_order = models.PositiveIntegerField(verbose_name=_("my_order"), default=0, blank=False, null=False)

    class Meta:
        ordering = ['my_order', ]
        verbose_name = _("TenantFAQ")
        verbose_name_plural = _("TenantFAQs")


class PartnerFAQ(models.Model):
    """Main page Partner FAQ"""
    question = models.CharField(verbose_name=_("question"), max_length=50)
    answer = models.CharField(verbose_name=_("answer"), max_length=50)
    my_order = models.PositiveIntegerField(verbose_name=_("my_order"), default=0, blank=False, null=False)

    class Meta:
        ordering = ['my_order', ]
        verbose_name = _("PartnerFAQ")
        verbose_name_plural = _("PartnerFAQs")
