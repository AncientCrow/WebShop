from datetime import datetime
from django.utils.timezone import now
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("author"))
    title = models.CharField(max_length=100, verbose_name=_("title"))
    description = models.TextField(max_length=10000, verbose_name=_("description"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"))
    created_at = models.DateField(editable=False, verbose_name=_("created date"), default=now())

    status_choices = [
        ("m", "У модерации"),
        ("a", "Активное"),
        ("i", "Неактивное"),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default="d", verbose_name=_("status"))

    class Meta:
        db_table = "services"
        ordering = ["created_at"]

    def get_absolute_url(self):
        return f"/services/{self.id}"

    def __str__(self):
        return self.title

    def short_description(self):
        return f"{self.description[:100]}..."


class Goods(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("author"))
    title = models.CharField(max_length=100, verbose_name=_("title"))
    description = models.TextField(max_length=10000, verbose_name=_("description"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"))
    created_at = models.DateField(verbose_name=_("created date"), editable=False, default=now())

    status_choices = [
        ("m", "У модерации"),
        ("a", "Активное"),
        ("i", "Неактивное"),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default="d", verbose_name=_("status"))

    class Meta:
        db_table = "goods"
        ordering = ["created_at"]

    def get_absolute_url(self):
        return f"/goods/{self.id}"

    def __str__(self):
        return self.title

    def short_description(self):
        return f"{self.description[:100]}..."


class GoodsImages(models.Model):
    image = models.ImageField(
        upload_to="goods/%Y_%m_%d",
        verbose_name=_("image")
    )
    product = models.ForeignKey(
        Goods,
        on_delete=models.CASCADE,
        related_name="goods_images",
        null=True
    )

    class Meta:
        db_table = "goods_files"


class ServicesImage(models.Model):
    image = models.ImageField(
        upload_to="services/%Y_%m_%d",
        verbose_name=_("image")
    )
    product = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="service_images",
        null=True
    )

    class Meta:
        db_table = "service_files"
