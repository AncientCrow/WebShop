from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
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
        return render(
            request, "shop/service_list.html", {
                "product_list": services_list,
                "images": services_image,
            }
        )


class GoodsList(View):

    def get(self, request, *args, **kwargs):
        goods_list = models.Goods.objects.all
        goods_image = models.GoodsImages.objects.all
        return render(
            request, "shop/goods_list.html", {
                "product_list": goods_list,
                "images": goods_image,
            }
        )


class GoodsDetail(DetailView):
    model = models.Goods
    template_name = "shop/product_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsDetail, self).get_context_data()
        context["files"] = models.GoodsImages.objects.all
        return context


class ServiceDetail(DetailView):
    model = models.Service
    template_name = "shop/product_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceDetail, self).get_context_data()
        context["files"] = models.ServicesImage.objects.all
        return context


class Privacy(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shop/privacy.html")


class About(View):

    def get(self, request, *args, **kwargs):
        return render(request, "shop/about_us.html")
