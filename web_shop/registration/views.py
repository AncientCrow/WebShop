import random

from django.db import transaction
from rest_framework.generics import ListAPIView
from django.db.models import Max, Count
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.cache import cache
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend

from . import forms, models, serializers, filters
from shop import models as shop_models
from registration import models as user_models


class RegistrationPage(View):
    """
    Класс отвечающий за отображение страницы с регистрацией нового пользователя
    """

    def get(self, request):
        registration = forms.RegistrationForm
        return render(request, "registration/registration.html", {'form': registration})

    def post(self, request):
        form = forms.RegistrationForm(request.POST, request.FILES)
        file = request.FILES.get("profile_icon")
        if form.is_valid():
            user = form.save()

            models.Profile.objects.create(
                user=user,
                icon=file,
            )

            new_user = authenticate(
                username=form.cleaned_data.get("username"),
                password=form.cleaned_data.get("password1")
            )
            login(request, new_user)
            user.save()
            return redirect("main")
        else:
            return render(request, "registration/registration.html", {'form': form})


class ProfileDetail(View):
    """
    Отображение детальной информации о профиле, с выводом случайных товаров как рекомендуемых.
    Рекомендуемые товары сохраняются в cache памяти. Имеется возможность обновления изображения профиля

    Methods
    ---------
        * get_random_goods() - метод, возвращающий случайно выбранный товар из БД
        * get_random_services() - метод, возвращающий случайно выбранную услугу из БД
    """

    @staticmethod
    def get_random_goods():
        max_id = shop_models.Product.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            goods = shop_models.Product.objects.filter(pk=pk).first()
            if goods:
                return goods
            else:
                return None

    @staticmethod
    def get_random_services():
        max_id = shop_models.Product.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            goods = shop_models.Product.objects.filter(pk=pk).first()
            if goods:
                return goods
            else:
                return None

    def get(self, request, pk):
        try:
            user = request.user.id
            page_user = get_object_or_404(models.Profile, user=user)
            product_1 = cache.get_or_set("product1", self.get_random_goods(), 3 * 60)
            product_2 = cache.get_or_set("product2", self.get_random_goods(), 3 * 60)
            product_3 = cache.get_or_set("product3", self.get_random_services(), 3 * 60)
            product_4 = cache.get_or_set("product4", self.get_random_services(), 3 * 60)
            author_products = user_models.Profile.objects.annotate(
                products=Count("product"),
            )
            goods = author_products[0].products
            balance_form = forms.UpdateBalance()
            return render(request, "profile/profile_detail.html", {
                "profile": page_user,
                "goods": goods,
                "balance_form": balance_form,
                "product1": product_1,
                "product2": product_2,
                "product3": product_3,
                "product4": product_4,
            })
        except Http404:
            return render(request, "profile/profile_detail.html", {"moderation": True})

    @transaction.atomic()
    def post(self, request, pk):
        form = forms.UpdateBalance(request.POST)
        if form.is_valid():
            profile = user_models.Profile.objects.get(user_id=request.user.id)
            balance = profile.balance
            profile.balance = form.cleaned_data.get("balance") + balance
            profile.save()
            return redirect("user_detail", pk)


class UserEdit(View):
    """
    Страница для редактирования профиля
    """

    def get(self, request, pk):
        form = forms.UpdateProfile
        return render(request, "profile/profile_edit.html", {"form": form})

    def post(self, request, pk):
        form = forms.UpdateProfile(request.POST, request.FILES)

        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            about = form.cleaned_data.get("about")
            icon = form.cleaned_data.get("icon")

            user = models.User.objects.get(id=request.user.id)
            user.first_name = first_name
            user.last_name = last_name
            profile = models.Profile.objects.get(id=pk)
            profile.about = about
            profile.icon = icon
            user.save()
            profile.save()
        else:
            print(form.errors)
        return redirect("user_detail", pk)


class LoginPage(LoginView):
    """
    Класс отвечающий за отображение страницы входа в систему,
    принимает шаблон и форму логина

    Attributes
    -----------
        * template_name - название используемого шаблона
        * authentication_form - форма для аутентификации пользователя
    """

    template_name = "registration/login.html"
    authentication_form = forms.LoginForm


class Logout(LogoutView):
    """
    Класс отвечающий за отображения страницы выхода из системы
    работает на внутренней структуре Джанго
    """


class UserListAPI(ListAPIView):
    """
    API с выводом информации о пользователях модели User,
    дополнительно выводится информация из модели Profile

    Attributes
    -----------
        * queryset - queryset содержащие все данные модели из БД
        * serializer_class - serializer для преобразования данных (в данном случае касательно пользователя)
        * filter_backends - выбор backend для фильтра API отображения
        * filterset_class - фильтр для списка пользователей
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.UsersFilter


class ProfileListApi(ListAPIView):
    """
    API с выводом информации о пользователях модели Profile

    Attributes
    -----------
        * queryset - queryset содержащие все данные модели из БД
        * serializer_class - serializer для преобразования данных (в данном случае касательно профиля пользователя)
        * filter_backends - выбор backend для фильтра API отображения
        * filterset_class - фильтр для списка пользователей
    """

    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.ProfileFilter
