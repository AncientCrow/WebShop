import django_filters as filters

from . import models


class GoodsFilter(filters.FilterSet):

    class Meta:
        model = models.Goods
        fields = {
            'price': ['gte', 'exact', 'lte', ],
            "author_id": ["exact", ],
            "title": ["exact", "contains", ]
        }


class ServicesFilter(filters.FilterSet):

    class Meta:
        model = models.Service
        fields = {
            "price": ["gte", "exact", "lte"],
            "author_id": ["exact", ],
            "title": ["exact", "contains", ]
        }