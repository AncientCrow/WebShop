from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime

from app_shop.models import Product
from app_registration.models import Profile


class ProductTest(TestCase):

    def setUp(self):
        User.objects.create_user(username="test",
                                 email="test@test.ru",
                                 password="123qwe!@#"
                                 )

        profile = Profile.objects.create(
            user=User(id=1),
            verify=True,
            balance=100,
            used_balance=100,
            status="C",
        )

        self.product = Product.objects.create(
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100,
        )
        self.product.authors.set([profile.pk, ])

    def test_title_max_length(self):
        post = Product.objects.get(id=self.product.id)
        max_length = post._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        post = Product.objects.get(id=self.product.id)
        max_length = post._meta.get_field("description").max_length
        self.assertEqual(max_length, 10000)

    def test_status_max_length(self):
        post = Product.objects.get(id=self.product.id)
        max_length = post._meta.get_field("status").max_length
        self.assertEqual(max_length, 1)

    def test_created_date_editable_false(self):
        post = Product.objects.get(id=self.product.id)
        editable = post._meta.get_field("created_at").editable
        self.assertFalse(editable)
