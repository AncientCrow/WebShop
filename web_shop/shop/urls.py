from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main"),
    path("services/", views.ServiceList.as_view(), name="services"),
    path("goods/", views.GoodsList.as_view(), name="goods"),
    path("goods/<int:pk>/", views.GoodsDetail.as_view(), name="goods_detail"),
    path("service/<int:pk>/", views.ServiceDetail.as_view(), name="service_detail"),
    path("privacy/", views.Privacy.as_view(), name="privacy"),
    path("contact/", views.MainPage.as_view(), name="contact"),
    path("about/", views.About.as_view(), name="about_us"),
    path("i18n", include("django.conf.urls.i18n")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
