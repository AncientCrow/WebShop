from .. import models
from django.test import TestCase
from django.contrib.auth.models import User
from datetime import datetime


class GoodsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test",
                                 email="test@test.ru",
                                 password="qwe123QWE"
                                 )
        cls.object_id = models.Goods.objects.create(
            author=User(id=1),
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100
        ).pk

    def test_title_max_length(self):
        post = models.Goods.objects.get(id=self.object_id)
        max_length = post._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        post = models.Goods.objects.get(id=self.object_id)
        max_length = post._meta.get_field("description").max_length
        self.assertEqual(max_length, 10000)

    def test_status_max_length(self):
        post = models.Goods.objects.get(id=self.object_id)
        max_length = post._meta.get_field("status").max_length
        self.assertEqual(max_length, 1)

    def test_created_date_editable_false(self):
        post = models.Goods.objects.get(id=self.object_id)
        editable = post._meta.get_field("created_at").editable
        self.assertFalse(editable)


class ServicesTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test",
                                 email="test@test.ru",
                                 password="123qwe!@#"
                                 )
        cls.object_id = models.Service.objects.create(
            author=User(id=1),
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100
        ).pk

    def test_title_max_length(self):
        post = models.Service.objects.get(id=self.object_id)
        max_length = post._meta.get_field("title").max_length
        self.assertEqual(max_length, 100)

    def test_description_max_length(self):
        post = models.Service.objects.get(id=self.object_id)
        max_length = post._meta.get_field("description").max_length
        self.assertEqual(max_length, 10000)

    def test_status_max_length(self):
        post = models.Service.objects.get(id=self.object_id)
        max_length = post._meta.get_field("status").max_length
        self.assertEqual(max_length, 1)

    def test_created_date_editable_false(self):
        post = models.Service.objects.get(id=self.object_id)
        editable = post._meta.get_field("created_at").editable
        self.assertFalse(editable)