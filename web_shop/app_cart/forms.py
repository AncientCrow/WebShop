from django import forms


class ProductsToCart(forms.Form):
    product_count = [(i, str(i)) for i in range(1, 21)]
    quantity = forms.TypedChoiceField(choices=product_count, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
