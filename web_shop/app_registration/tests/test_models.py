from django.test import TestCase
from django.contrib.auth.models import User

from app_registration.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="test",
            email="test@test.ru",
            password="123qwe!@#"
        )
        self.profile = Profile.objects.create(
            user=User(id=1),
            verify=True,
            balance=100,
            used_balance=100,
            status="C",
        )

    def test_absolute_url(self):
        user = Profile.objects.get(balance=100)
        self.assertEquals(user.get_absolute_url(), '/user/1')

    def test_common_status_check(self):
        user = Profile.objects.get(id=self.profile.id)
        user.used_balance = 1500
        user.check_status()
        self.assertEqual(user.status, "C")

    def test_advanced_status_check(self):
        user = Profile.objects.get(id=self.profile.id)
        user.used_balance = 15000
        user.check_status()
        self.assertEqual(user.status, "A")

    def test_vip_status_check(self):
        user = Profile.objects.get(id=self.profile.id)
        user.used_balance = 25000
        user.check_status()
        self.assertEqual(user.status, "V")
