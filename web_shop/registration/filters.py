import django_filters as filters
from django.contrib.auth.models import User
from . import models


class UsersFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = {
            "username": ["exact", ]
        }

class ProfileFilter(filters.FilterSet):

    class Meta:
        model = models.Profile
        fields = {
            "user": ["exact", ]
        }
