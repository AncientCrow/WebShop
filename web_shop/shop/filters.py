import django_filters as filters

from . import models


class ProductFilter(filters.FilterSet):
    """
    Реализация фильтра для списка товаров с помощью django-filter
    """

    class Meta:
        model = models.Product
        fields = {
            'price': ['gte', 'exact', 'lte', ],
            "title": ["exact", "contains", ]
        }
