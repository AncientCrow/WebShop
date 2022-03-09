from django import forms
from django.utils.translation import gettext_lazy as _
from . import models


class GoodsForm(forms.ModelForm):
    title = forms.CharField(label=_("Title"))
    description = forms.CharField(widget=forms.Textarea, label=_("Description"))

    class Meta:
        model = models.Goods
        fields = ["title", "description"]


class GoodsImageForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'multiple': True}),
        required=True,
        label=_("Images to upload"),
    )

    class Meta:
        model = models.GoodsImages
        fields = ["images"]


class ServicesForm(forms.ModelForm):
    title = forms.CharField(label=_("Title"))
    description = forms.CharField(widget=forms.Textarea, label=_("Description"))

    class Meta:
        model = models.Service
        fields = ["title", "description"]


class ServicesImageForm(forms.ModelForm):
    images = forms.FileField(
        widget=forms.ClearableFileInput(
            attrs={'multiple': False}),
        required=True,
        label=_("Images to upload"),
    )

    class Meta:
        model = models.ServicesImage
        fields = ["images"]
