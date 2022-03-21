from django.contrib import admin
from . import models


class GoodsImageInline(admin.TabularInline):
    """
    Добавление инлайн модуля для модели Goods в админ-панели
    """
    model = models.GoodsImages
    extra = 0


class ServiceImageInline(admin.TabularInline):
    """
    Добавление инлайн модуля для модели Service в админ-панели
    """
    model = models.ServicesImage
    extra = 0

@admin.register(models.Goods)
class GoodsAdmin(admin.ModelAdmin):
    """
    Регистрация модели Goods в админ-панели
    """
    all_fields = [field.name for field in models.Goods._meta.fields if field.name != "description"]
    list_display = all_fields
    inlines = [GoodsImageInline]


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Регистрация модели Service в админ-панели
    """
    all_fields = [field.name for field in models.Service._meta.fields if field.name != "description"]
    list_display = all_fields
    inlines = [ServiceImageInline]

