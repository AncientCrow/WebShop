from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(models.Goods)
class GoodsTranslationOptions(TranslationOptions):
    fields = ("title", "description")
