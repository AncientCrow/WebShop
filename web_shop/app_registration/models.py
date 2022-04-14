from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """
    Модель содержащая информацию о пользователе

    Attributes
    -----------
        * user - внешний ключ связанный с внутренней моделью User
        * city - текстовое(символьное) поле с информацией о городе пользователя
        * about - текстовое поле с информацией о пользователе
        * date - поле с календарной датой рождения пользователя
        * phone_regex - регулярное выражение для обработки номеров телефона
        * phone - текстовое(символьное) поле для номера телефона пользователя
        * balance - числовое поле для указания баланса пользователя
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"), related_name="user_id")
    verify = models.BooleanField(default=False, verbose_name=_("verification"))
    balance = models.IntegerField(default=0, verbose_name=_("balance"))
    icon = models.ImageField(upload_to="users/%Y_%m_%d", null=True, verbose_name=_("icon"))
    used_balance = models.IntegerField(default=0, verbose_name=_("balance"))
    status_choices = [
        ("C", "Обычный"),
        ("A", "Продвинутый"),
        ("V", "VIP"),
    ]
    status = models.CharField(max_length=1, choices=status_choices, default="C", verbose_name=_("status"))

    class Meta:
        permissions = (
            ("verified", "Верифицирован"),
        )
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
        unique_together = ["user", "id"]
        ordering = ["id"]

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return f"/user/{self.id}"

    def check_status(self):
        if 0 < self.used_balance < 10000:
            self.status = "C"
        elif 10000 < self.used_balance < 20000:
            self.status = "A"
        elif self.used_balance > 20000:
            self.status = "V"

    def update_balance(self, balance):
        if self.balance >= balance:
            self.balance -= balance
            self.used_balance += balance
            self.check_status()
            self.save()
            return True
        elif self.balance <= balance:
            return False
