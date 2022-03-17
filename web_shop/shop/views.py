from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView

from . import models, serializers


class MainPage(View):
    """
    Класс отвечающий за отображение главной страницы, является наследником View
    """

    def get(self, request):
        return render(request, "shop/main_page.html")


class ServiceList(View):
    """
    Класс, отвечающий за отображения списка услуг. Получает данные об услуге из одной модели,
    изображения подгружаются из другой модели (возможно использование нескольких изображений),
    но на текущий момент функция отключена
    """
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
    """
    Класс, отвечающий за отображения списка товаров. Получает данные о товаре из одной модели,
    изображения подгружаются из другой модели (возможно использование нескольких изображений),
    но на текущий момент функция отключена
    """

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
    """
    Класс, отвечающий за детальное отображение товара.
    Для подгрузки изображений используется het_context_data()
    """


    model = models.Goods
    template_name = "shop/product_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GoodsDetail, self).get_context_data()
        context["files"] = models.GoodsImages.objects.all
        return context


class ServiceDetail(DetailView):
    """
    Класс, отвечающий за детальное отображение услуги.
    Для подгрузки изображений используется het_context_data()
    """
    model = models.Service
    template_name = "shop/product_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ServiceDetail, self).get_context_data()
        context["files"] = models.ServicesImage.objects.all
        return context


class Privacy(View):
    """ Отображение страницы с политикой конфеденциальности """
    def get(self, request, *args, **kwargs):
        return render(request, "shop/privacy.html")


class About(View):
    """ Отображение страницы с информацией 'о нас' """
    def get(self, request, *args, **kwargs):
        return render(request, "shop/about_us.html")


class GoodsAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    API страница со списком товаров, имеется фильтрация по названию товара,
    автору, цене (включая сортирову по убыванию/возрастанию)
    """

    queryset = models.Goods.objects.all()
    serializer_class = serializers.GoodsSerializer

    def get_queryset(self):
        queryset = models.Goods.objects.all()
        goods_author = self.request.query_params.get("author")
        goods_title = self.request.query_params.get("title")
        goods_price = self.request.query_params.get("price")

        if goods_author:
            queryset = queryset.filter(author=goods_author)
        elif goods_title:
            queryset = queryset.filter(title=goods_title)
        elif goods_price:
            if goods_price == "up":
                queryset = queryset.filter().order_by("price")
            elif goods_price == "down":
                queryset = queryset.filter().order_by("-price")
                try:
                    queryset = queryset.filter(price=goods_price)
                except ValueError:
                    queryset = queryset.filter().order_by("price")

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DetailGoodsAPIView(RetrieveModelMixin,
                         UpdateModelMixin,
                         DestroyModelMixin,
                         GenericAPIView):
    """
    API страница с детальной информацией о товаре
    """
    queryset = models.Goods.objects.all()
    serializer_class = serializers.ServicesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DetailServiceAPIView(RetrieveModelMixin,
                           UpdateModelMixin,
                           DestroyModelMixin,
                           GenericAPIView):

    """
    API страница с детальной информацией об услуге
    """

    queryset = models.Service.objects.all()
    serializer_class = serializers.ServicesSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class ServicesAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    API страница со списком услуг, имеется фильтрация по названию услуги,
    автору, цене (включая сортирову по убыванию/возрастанию)
    """
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServicesSerializer

    def get_queryset(self):
        queryset = models.Service.objects.all()
        service_author = self.request.query_params.get("author")
        service_title = self.request.query_params.get("title")
        service_price = self.request.query_params.get("price")

        if service_author:
            queryset = queryset.filter(author=service_author)
        elif service_title:
            queryset = queryset.filter(title=service_title)
        elif service_price:
            if service_price == "up":
                queryset = queryset.filter().order_by("price")
            elif service_price == "down":
                queryset = queryset.filter().order_by("-price")
            else:
                try:
                    queryset = queryset.filter(price=service_price)
                except ValueError:
                    queryset = queryset.filter().order_by("price")

        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
