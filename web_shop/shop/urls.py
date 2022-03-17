from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main"),
    path("services/", views.ServiceList.as_view(), name="services"),
    path("services_api/", views.ServicesAPIView.as_view(), name="services_api"),
    path("services_api/<int:pk>", views.DetailServiceAPIView.as_view(), name="services_api_detail"),
    path("goods/", views.GoodsList.as_view(), name="goods"),
    path("goods_api/", views.GoodsAPIView.as_view(), name="goods_api"),
    path("goods_api/<int:pk>", views.DetailGoodsAPIView.as_view(), name="goods_api_detail"),
    path("goods/<int:pk>/", views.GoodsDetail.as_view(), name="goods_detail"),
    path("service/<int:pk>/", views.ServiceDetail.as_view(), name="service_detail"),
    path("privacy/", views.Privacy.as_view(), name="privacy"),
    path("contact/", views.About.as_view(), name="contact"),
    path("about/", views.About.as_view(), name="about_us"),
    path("i18n", include("django.conf.urls.i18n")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
