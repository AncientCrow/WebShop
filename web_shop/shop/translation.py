from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Product)
class ProductTranslationOptions(TranslationOptions):
    """
    Класс для перевода значений модели в БД

    Attributes
    -----------
        * fileds - кортеж с данными о полях модели для перевода
    """

    fields = ('title', 'description')

