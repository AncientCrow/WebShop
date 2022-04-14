from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.http import require_POST
from django.db import transaction
from app_shop.models import Product
from app_registration.models import Profile
from app_cart.cart import Cart
from app_cart.forms import ProductsToCart


@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = ProductsToCart(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        cart.add(
            product=product,
            quantity=data["quantity"],
            update_quantity=data["update"],
        )

    return redirect("cart:cart_detail")


def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


class CartDetail(View):

    def get(self, request):
        cart = Cart(request)

        return render(request, 'cart_detail.html', {'app_cart': cart})

    @transaction.atomic()
    def post(self, request):
        cart = Cart(request)
        user = Profile.objects.get(user_id=request.user.id)
        balance = cart.get_total_price()
        update = user.update_balance(balance)
        print(update)
        if update:
            return redirect("main")
        else:
            return redirect("cart:cart_detail")
