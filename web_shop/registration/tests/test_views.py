from datetime import datetime
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .. import models
from shop import models as product


class RegistrationTest(TestCase):

    def test_url_exist(self):
        response = self.client.get("/registration/")
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("registration"))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("registration"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/registration.html")

    def test_new_user_registration(self):
        with open("files/users/2022_03_07/mem.png", "rb") as file:
            form_data = {
                "profile_icon": file,
                "username": "test",
                "first_name": "Bob",
                "last_name": "Ivanov",
                "password1": "123qwe!@#",
                "password2": "123qwe!@#",
                "email": "testagain@test.com",
                "date": "1902-01-01",
            }
            response = self.client.post(reverse("registration"), data=form_data)
            self.assertRedirects(response, reverse("main"))
            self.assertEqual(models.User.objects.count(), 1)


class ProfileDetailTest(TestCase):

    @classmethod
    def setUp(cls):
        User.objects.create_user(username="test", email="test@test.ru", password="123qwe!@#")
        cls.object_id = models.Profile.objects.create(
            user=User(id=1),
            city="Testcityname",
            date=datetime.now(),
            phone="88005553535",
            verify=True,
            balance=100,
        )
        models.ProfileIcon.objects.create(
            user=User(id=1),
            icon="files/users/2022_03_07/mem.png"
        )
        product.Service.objects.create(
            author=User(id=1),
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100
        )
        product.Goods.objects.create(
            author=User(id=1),
            title="Test title",
            description="Test description",
            created_at=datetime.now(),
            status="a",
            price=100
        )

    def test_url_exist(self):
        self.client.login(username="test", password="123qwe!@#")
        response = self.client.get("/user/1/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        self.client.login(username="test", password="123qwe!@#")
        response = self.client.get(reverse("user_detail", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        self.client.login(username="test", password="123qwe!@#")
        response = self.client.get(reverse("user_detail", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile/profile_detail.html")


class UserEditTest(TestCase):

    def test_url_exist(self):
        response = self.client.get("/user/1/edit/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("user_edit", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
        response = self.client.get(reverse("user_edit", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profile/profile_edit.html")
