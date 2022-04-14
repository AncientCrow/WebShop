import django_filters as filters

from app_shop.models import Product


class ProductFilter(filters.FilterSet):
    """
    Реализация фильтра для списка товаров с помощью django-filter
    """

    class Meta:
        model = Product
        fields = {
            'price': ['gte', 'exact', 'lte', ],
            "title": ["exact", "contains", ]
        }
