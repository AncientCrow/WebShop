import csv
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import datetime
from .. import models


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


class GoodsListTest(TestCase):

    def test_url_exist(self):
        response = self.client.get("/goods/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("goods"))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("goods"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/goods_list.html")


class GoodsDetailTest(TestCase):

    def setUp(self):
        User.objects.create_user(username="test",
                                 email="test@test.ru",
                                 password="qwe123QWE"
                                 )

        models.Goods.objects.create(
            author=User(id=1),
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100,
        )

    def test_url_exist(self):
        response = self.client.get("/goods/1/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("goods_detail", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("goods_detail", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product_detail.html")


class ServicesListTest(TestCase):

    def test_url_exist(self):
        response = self.client.get("/services/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("services"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/service_list.html")


class ServicesDetailTest(TestCase):

    def setUp(self):
        User.objects.create_user(username="test",
                                 email="test@test.ru",
                                 password="qwe123QWE"
                                 )

        models.Service.objects.create(
            author=User(id=1),
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100,
        )

    def test_url_exist(self):
        response = self.client.get("/service/1/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("service_detail", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("service_detail", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shop/product_detail.html")
