from django.contrib import admin
from app_shop.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in Product._meta.fields]
    list_display = all_fields
