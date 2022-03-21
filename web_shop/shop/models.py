from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    """
    Модель услуги

    Attributes
    -----------
        * author -  поле с внешним ключом к модели User
        * title - текстовое(символьное) пол с максимальной длинной в 100 знаков, содержит название услуги
        * description - текстовое поле с максимальной длиной в 10**4 знаков
        * price - поле с положительным числовым значением, по умолчанию = 0
        * created_at: поле со значением календаря
        * status - текстовое(символьное) поле обозначающее статус записи в системе m-у модерации, a-активное, i-неактивное

    Methods
    ---------
        * get_absolute_url - метод возвращающий адресс конкретного элемента модели в БД по его ID
        * short_description - метод возвращающий краткое описание услуги (100 знаков)
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("author"))
    title = models.CharField(max_length=100, verbose_name=_("title"))
    description = models.TextField(max_length=10000, verbose_name=_("description"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"))
    created_at = models.DateField(editable=False, verbose_name=_("created date"), default=None, null=True)

    status_choices = [
        ("m", "У модерации"),
        ("a", "Активное"),
        ("i", "Неактивное"),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default="d", verbose_name=_("status"))

    class Meta:
        db_table = "services"
        ordering = ["created_at"]

    def get_absolute_url(self) -> str:
        return f"/services/{self.id}"

    def __str__(self):
        return self.title

    def short_description(self) -> str:
        return f"{self.description[:100]}..."


class Goods(models.Model):
    """
    Модель товара

    Attributes
    -----------
        * author -  поле с внешним ключом к модели User
        * title - текстовое(символьное) пол с максимальной длинной в 100 знаков, содержит название товара
        * description - текстовое поле с максимальной длиной в 10**4 знаков
        * price - поле с положительным числовым значением, по умолчанию = 0
        * created_at - поле со значением календаря
        * status - текстовое(символьное) поле обозначающее статус записи в системе m-у модерации, a-активное, i-неактивное

    Methods
    ----------
        * get_absolute_url - метод возвращающий адресс конкретного элемента модели в БД по его ID
        * short_description - метод возвращающий краткое описание товара (100 знаков)
    """

    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("author"))
    title = models.CharField(max_length=100, verbose_name=_("title"))
    description = models.TextField(max_length=10000, verbose_name=_("description"))
    price = models.PositiveIntegerField(default=0, verbose_name=_("price"))
    created_at = models.DateField(editable=False, verbose_name=_("created date"), default=None, null=True)

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
    """
    Модель изображения товара

    Attributes
    -----------
        * image - поле для загрузки изображения (требуется Pillow), сохраняется по указанному пути
        * product - внешний ключ к модели Goods
    """

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
    """
    Модель изображения услуги

    Attributes
    -----------
        * image - поле для загрузки изображения (требуется Pillow), сохраняется по указанному пути
        * product - внешний ключ к модели Service
    """

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
