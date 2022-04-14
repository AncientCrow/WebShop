from django.urls import re_path
from app_cart import views

app_name = "cart"
urlpatterns = [
    re_path(r'^$', views.CartDetail.as_view(), name='cart_detail'),
    re_path(r'^add/(?P<product_id>\d+)/$', views.add_to_cart, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', views.remove_from_cart, name='cart_remove'),
]