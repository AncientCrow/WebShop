from modeltranslation.translator import register, TranslationOptions
from app_shop.models import Product


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    """
    Класс для перевода значений модели в БД

    Attributes
    -----------
        * fileds - кортеж с данными о полях модели для перевода
    """

    fields = ('title', 'description')

