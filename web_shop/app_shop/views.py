from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from app_shop import models, serializers, filters
from app_cart.forms import ProductsToCart


class MainPage(View):
    """
    Класс отвечающий за отображение главной страницы, является наследником View
    """

    def get(self, request):
        return render(request, "shop/main_page.html")


class ProductList(View):
    """
    Класс, отвечающий за отображения списка товаров. Получает данные о товаре из одной модели
    """

    def get(self, request, *args, **kwargs):
        product_list = models.Product.objects.only("title", "description").all()
        paginator = Paginator(product_list, 2)
        page = request.GET.get("page")
        pages = paginator.get_page(page)
        return render(
            request, "shop/product_list.html", {
                "product_list": pages,
            }
        )


class ProductDetail(DetailView):
    """
    Класс, отвечающий за детальное отображение товара.

    Attributes
    -----------
        * model - название модели для детального отображения
        * template_name - название шаблона для отображения

    Methods
    ---------
        * get_context_data - метод для добавления дополнительной информации, в данном случае изображения
    """

    model = models.Product
    template_name = "shop/product_detail.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context["app_cart"] = ProductsToCart()
        return context


class Privacy(View):
    """ Отображение страницы с политикой конфеденциальности """

    def get(self, request, *args, **kwargs):
        return render(request, "app_shop/privacy.html")


class About(View):
    """ Отображение страницы с информацией 'о нас' """

    def get(self, request, *args, **kwargs):
        return render(request, "shop/about_us.html")


class ProductAPIView(ListAPIView):
    """
    API страница со списком товаров, имеется фильтрация по названию товара,
    автору, цене (включая сортирову по убыванию/возрастанию)

    Attributes
    -----------
        * queryset - queryset содержащие все данные модели из БД
        * serializer_class - serializer для преобразования данных (в данном случае касательно товаров)
        * filter_backends - выбор backend для фильтра API отображения
        * filterset_class - фильтр для списка товаров
    """

    queryset = models.Product.objects.prefetch_related("authors").all()
    serializer_class = serializers.ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.ProductFilter


class DetailProductAPIView(RetrieveModelMixin,
                           UpdateModelMixin,
                           DestroyModelMixin,
                           GenericAPIView):
    """
    API страница с детальной информацией о товаре

    Attributes
    -----------
        * queryset - queryset содержащие все данные модели из БД
        * serializer_class - serializer для преобразования данных (в данном случае касательно товара)
    """
    queryset = models.Product.objects.prefetch_related("authors").all()
    serializer_class = serializers.ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
