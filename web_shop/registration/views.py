import random

from rest_framework.generics import ListAPIView
from django.db.models import Max
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
            date = form.cleaned_data.get('date')
            city = form.cleaned_data.get('city')

            models.ProfileIcon.objects.create(
                user=user,
                icon=file,
            )

            models.Profile.objects.create(
                user=user,
                city=city,
                date=date
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
    """

    @staticmethod
    def get_random_goods():
        max_id = shop_models.Goods.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            goods = shop_models.Goods.objects.filter(pk=pk).first()
            if goods:
                return goods

    @staticmethod
    def get_random_services():
        max_id = shop_models.Service.objects.all().aggregate(max_id=Max("id"))['max_id']
        while True:
            pk = random.randint(1, max_id)
            goods = shop_models.Service.objects.filter(pk=pk).first()
            if goods:
                return goods

    def get(self, request, pk):
        try:
            user = request.user.id
            page_user = get_object_or_404(models.Profile, user_id=user)
            user_icon = models.ProfileIcon.objects.filter(user_id=user).get()
            form = forms.UpdateIcon
            product_1 = cache.get_or_set("product1", self.get_random_goods(), 30 * 60)
            product_2 = cache.get_or_set("product2", self.get_random_goods(), 30 * 60)
            product_3 = cache.get_or_set("product3", self.get_random_services(), 30 * 60)
            product_4 = cache.get_or_set("product4", self.get_random_services(), 30 * 60)

            return render(request, "profile/profile_detail.html", {
                "profile": page_user,
                "icon": user_icon,
                "form": form,
                "product1": product_1,
                "product2": product_2,
                "product3": product_3,
                "product4": product_4,
            })
        except Http404:
            return render(request, "profile/profile_detail.html", {"moderation": True})

    def post(self, request, pk, *args, **kwargs):
        form = forms.UpdateIcon(request.POST, request.FILES)
        print(pk)
        if form.is_valid():
            icon = form.cleaned_data.get("profile_icon")
            models.ProfileIcon.objects.filter(id=pk).update_or_create(
                icon=icon,
                user=pk
            )
        return redirect("user_detail", pk)


class UserEdit(View):
    """
    Страница для редактирования профиля
    """
    def get(self, request, pk):
        form = forms.UpdateProfile
        return render(request, "profile/profile_edit.html", {"form": form})

    def post(self, request, pk):
        form = forms.UpdateProfile(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            about = form.cleaned_data.get("about")
            models.User.objects.filter(id=request.user.id).update(
                first_name=first_name,
                last_name=last_name,
            )
            models.Profile.objects.filter(id=pk).update(
                about=about
            )
            return redirect("user_detail", pk)


class LoginPage(LoginView):
    """
    Класс отвечающий за отображение страницы входа в систему,
    принимает шаблон и форму логина
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
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.UsersFilter



class ProfileListApi(ListAPIView):
    """
    API с выводом информации о пользователях модели Profile
    """
    queryset = models.Profile.objects.all()
    serializer_class = serializers.ProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.ProfileFilter

