from django.contrib import admin
from django.contrib.auth.models import User
from app_registration.models import Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Регистрация модели Profile в админ-панели

    Attributes
    -----------
        * list_display - столбцы отображаемые в админ-панели
        * actions - доступные действия

    Methods
    ----------
        * add_verify_permission() - верификация пользователя сменой Boolean значения verify на True
    """

    list_display = ('user', "verify")
    actions = ["add_verify_permission"]

    def add_verify_permission(self, request, queryset):
        queryset.update(verify=True)

    add_verify_permission.short_description = "Верифицировать"


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
