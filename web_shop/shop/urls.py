from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.MainPage.as_view(), name="main"),
    path("product/", views.ProductList.as_view(), name="products"),
    path("product_api/", views.ProductAPIView.as_view(), name="product_api"),
    path("product_api/<int:pk>", views.DetailProductAPIView.as_view(), name="product_api_detail"),
    path("product/<int:pk>/", views.ProductDetail.as_view(), name="product_detail"),
    path("privacy/", views.Privacy.as_view(), name="privacy"),
    path("contact/", views.About.as_view(), name="contact"),
    path("about/", views.About.as_view(), name="about_us"),
    path("i18n", include("django.conf.urls.i18n")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
