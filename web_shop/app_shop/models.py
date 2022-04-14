from django.db import models
from django.utils.translation import gettext_lazy as _
from app_registration.models import Profile


class Product(models.Model):
    """
    Модель товара

    Attributes
    -----------
        * product - внешний ключ для определения общего id
        * title - текстовое(символьное) пол с максимальной длинной в 100 знаков, содержит название товара
        * description - текстовое поле с максимальной длиной в 10**4 знаков
        * price - поле с положительным числовым значением, по умолчанию = 0
        * created_at - поле со значением календаря
        * status - текстовое(символьное) поле обозначающее статус записи в системе
          m-'у модерации', a-'активное', i-'неактивное'
        * image - изображение для товара

    Methods
    ----------
        * get_absolute_url - метод возвращающий адресс конкретного элемента модели в БД по его ID
        * short_description - метод возвращающий краткое описание товара (100 знаков)
    """
    authors = models.ManyToManyField(Profile)
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
    image = models.ImageField(
        upload_to="services/%Y_%m_%d",
        verbose_name=_("image"),
        null=True,
    )

    def get_absolute_url(self) -> str:
        return f"/product/{self.id}"

    def short_description(self) -> str:
        return f"{self.description[:100]}..."

    class Meta:
        db_table = "product"
        ordering = ["id"]

    def __str__(self):
        return f"Товар '{self.title}'"
