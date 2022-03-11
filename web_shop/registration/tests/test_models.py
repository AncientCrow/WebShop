from django.test import TestCase
from django.contrib.auth.models import User
from .. import models
from datetime import datetime
import re


class ProfileModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username="test", email="test@test.ru", password="123qwe!@#")
        cls.object_id = models.Profile.objects.create(
            user=User(id=1),
            city="Testcityname",
            date=datetime.now(),
            phone="88005553535",
            verify=True,
            balance=100,
        ).pk

    def test_phone_format(self):
        user = models.Profile.objects.get(id=self.object_id)
        phone_regex = r"^\+?1?\d{8,15}$"
        phone = user._meta.get_field('phone')
        phone_value = phone.value_from_object(user)
        phone_value_test = re.match(phone_regex, phone_value)
        self.assertIsNot(phone_value_test, None)

    def test_city_name_length(self):
        user = models.Profile.objects.get(id=self.object_id)
        max_length = user._meta.get_field('city').max_length
        self.assertEqual(max_length, 36)

    def test_absolute_url(self):
        user = models.Profile.objects.get(id=self.object_id)
        self.assertEquals(user.get_absolute_url(), '/user/1')
