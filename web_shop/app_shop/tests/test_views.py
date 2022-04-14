from datetime import datetime

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from app_shop.models import Product
from app_registration.models import Profile

from django.db.backends.postgresql.features import DatabaseFeatures


DatabaseFeatures.can_defer_constraint_checks = False


class MainPageTest(TestCase):

    def test_url_exist(self):
        response = self.client.get("/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("main"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/main_page.html")


class ProductListTest(TestCase):

    def test_url_exist(self):
        response = self.client.get("/product/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("products"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product_list.html")


class ProductDetailTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(
            username="Silver",
            email="test@test.com",
            password="123qwe!@#"
        )

        profile = Profile.objects.create(
            user=User(id=1),
            verify=True,
            balance=100,
            used_balance=100,
            status="C",
        )

        product = Product.objects.create(
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100,
        )
        product.authors.set([profile.pk, ])

    def test_url_exist(self):
        response = self.client.get(f"/product/6/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("product_detail", kwargs={'pk': 6}))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("product_detail", kwargs={'pk': 6}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product_detail.html")
