import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegistrationForm(UserCreationForm):
    """
    Форма регистрации, содержит поля для никнейма, имени, фамилии, даты рождения
    а также пароля. Дата рождения выбирается на основе текущий год - 120 лет
    (на всякий случай, для долгожителей)

    Attributes
    -----------
        * profile_icon - поле для добавление изображения профиля
        * username - текстовое(символьное) поле для ввода никнейма (максимальная длина 25 символов)
        * first_name - текстовое(символьное) поле для ввода имени (максимальная длина 25 символов)
        * last_name - текстовое(символьное) поле для ввода фамилии (максимальная длина 30 символов)
        * password1 - текстовое(символьное) поле для ввода пароля
        * password2 - текстовое(символьное) поле для ввода подтверждения пароля
        * email - специальное Email поля, для воода электронной почты
        * start_year - стартовое значение года рождения
        * end_year - конечное значение года рождения
        * date - поле с выбором даты рождения
        * phone - текстовое(символьное) поле для сохранения номера телефона
        * city - текстовое(символьное) поле для ввода названия города

    """
    profile_icon = forms.ImageField(required=False, label=_("Profile icon"))
    username = forms.CharField(label=_("Nickname"), max_length=25)
    first_name = forms.CharField(label=_("First name"), max_length=25)
    last_name = forms.CharField(label=_("Last name"), max_length=30)
    password1 = forms.CharField(label=_("Password"), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirm"), widget=forms.PasswordInput)
    email = forms.EmailField(label=_("Email"), required=False)
    start_year = datetime.date.today().year - 120
    end_year = datetime.date.today().year
    date = forms.DateField(
        label=_("Birthday"),
        widget=forms.SelectDateWidget(years=range(start_year, end_year)),
    )
    phone = forms.CharField(label=_("Phone number"), max_length=16, required=False)
    city = forms.CharField(label=_("Your city"), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date']


class LoginForm(AuthenticationForm):
    """
    Форма для отображения на странице аутентификации пользователя, содержит
    поля для ввода логина/пароля

    Attributes
    -----------
        * username - текстовое(символьное) поле для вводна никнейма
        * password - текстовое(символьное) поле для ввода пароля
        * error_messages - словарь с возможными ошибками и ответом на эти ошибки
    """
    username = forms.CharField(label=_("Nickname"), widget=forms.TextInput())
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput())
    error_messages = {
        'invalid_login': _("Incorrect login or password"),
        'inactive': _("Your profile deactivated"),
    }


class UpdateProfile(forms.Form):
    """
    Форма для обновления информации о пользователе

    Attributes
    -----------
        * first_name - текстовое(символьное) поле для ввода имени
        * last_name - текстовое(символьное) поле для ввода фамилии
        * about - текстовое поле для ввода информации о себе
    """

    first_name = forms.CharField(label=_("First name"), max_length=25)
    last_name = forms.CharField(label=_("Last name"), max_length=30)
    about = forms.CharField(label=_("About"), max_length=10000, widget=forms.Textarea())


class UpdateIcon(forms.Form):
    """
    Форма для обновления изображения профиля

    Attributes
    -----------
        * icon - поле для добавления файла изображения
    """
    icon = forms.ImageField(label=_("Image"))
