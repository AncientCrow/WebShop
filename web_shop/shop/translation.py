from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Service)
class ServiceTranslationOptions(TranslationOptions):
    """
    Класс для перевода значений модели в БД

    Attributes
    -----------
        * fileds - кортеж с данными о полях модели для перевода
    """

    fields = ('title', 'description')


@register(models.Goods)
class GoodsTranslationOptions(TranslationOptions):
    """
    Класс для перевода значений модели в БД

    Attributes
    -----------
        * fileds - кортеж с данными о полях модели для перевода
    """

    fields = ("title", "description")
