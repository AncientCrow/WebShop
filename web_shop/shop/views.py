from django.shortcuts import render
from django.views import View
from . import models


class MainPage(View):
    """
    Класс отвечающий за отображение главной страницы, является наследником View

    Methods:
    ________
    get - на текущий момент принимает get запрос и выдает шаблон main-page.html

    """

    def get(self, request):
        return render(request, "shop/main_page.html")


class ServiceList(View):

    def get(self, request, *args, **kwargs):
        services_list = models.Service.objects.all
        services_image = models.ServicesImage.objects.all
        return render(request, "shop/services_list.html", {
            "services_list": services_list,
            "images": services_image,
        })


class GoodsList(View):

    def get(self, request, *args, **kwargs):
        goods_list = models.Goods.objects.all
        goods_image = models.GoodsImages.objects.all
        return render(
            request, "shop/goods_list.html", {
                "goods_list": goods_list,
                "images": goods_image,
            }
        )


class Privacy(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shop/privacy.html")


class About(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shop/about_us.html")