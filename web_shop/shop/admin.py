from django.contrib import admin
from . import models


class GoodsImageInline(admin.TabularInline):
    model = models.GoodsImages
    extra = 0


@admin.register(models.Goods)
class GoodsAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.Goods._meta.fields if field.name != "description"]
    list_display = all_fields
    inlines = [GoodsImageInline]

