import django_filters as filters
from django.contrib.auth.models import User
from app_registration.models import Profile


class UsersFilter(filters.FilterSet):
    """
    Реализация фильтра для списка пользователей с помощью django-filter
    """

    class Meta:
        model = User
        fields = {
            "username": ["exact", ]
        }


class ProfileFilter(filters.FilterSet):
    """
    Реализация фильтра для списка профилей пользователей с помощью django-filter
    """

    class Meta:
        model = Profile
        fields = {
            "user": ["exact", ]
        }
