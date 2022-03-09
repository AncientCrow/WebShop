from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth import authenticate, login
from . import forms, models


class RegistrationPage(View):
    """
    Класс отвечающий за отображение страницы с регистрацией нового пользователя

    Methods:
    ________
    get - принимает get запрос и выдает шаблон registration.html с формой регистрации
    ( из forms.RegistrationForm в шаблоне используется как {{ form }} )
    post - принимает post запрос c данными о пользователе, которые были в форме регистрации
    Создается объект registration в виде форме с заполненными данными (благодаря request.POST)
    Если is_valid == True, то данные сохраняются в бд
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

    def get(self, request, pk):
        try:
            user = request.user.id
            page_user = get_object_or_404(models.Profile, user_id=user)
            user_icon = models.ProfileIcon.objects.filter(user_id=user).get()
            form = forms.UpdateIcon
            return render(request, "profile/profile_detail.html", {
                "profile": page_user,
                "icon": user_icon,
                "form": form
            })
        except Http404:
            return render(request, "registration/profile_detail.html", {"moderation": True})

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

    def get(self, request, pk):
        form = forms.UpdateProfile
        return render(request, "registration/profile_edit.html", {"form": form})

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