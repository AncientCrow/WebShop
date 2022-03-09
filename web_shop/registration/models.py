from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("user"))
    city = models.CharField(max_length=36, null=True, verbose_name=_("city"))
    about = models.TextField(max_length=10000, null=True, verbose_name=_("about"))
    date = models.DateField(verbose_name=_("date"))
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phone_regex], max_length=16, unique=True, null=True, verbose_name=_("phone"))
    verify = models.BooleanField(default=False, verbose_name=_("verification"))

    class Meta:
        permissions = (
            ("verified", "Верифицирован"),
        )
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def get_absolute_url(self):
        return f"/user/{self.id}"


class ProfileIcon(models.Model):
    icon = models.ImageField(upload_to="users")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "user_icon"
