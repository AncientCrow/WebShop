from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    all_fields = [field.name for field in models.Product._meta.fields]
    list_display = all_fields
