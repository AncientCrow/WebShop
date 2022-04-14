from datetime import datetime

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from app_shop.models import Product
from app_registration.models import Profile
from web_shop.settings import BASE_DIR


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
        image_path = BASE_DIR + "/files/users/test/test.jpg"
        form_data = {
            "profile_icon": SimpleUploadedFile(
                name="mem.png",
                content=open(image_path, "rb").read(),
                content_type='image/jpg'
            ),
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
        self.assertEqual(User.objects.count(), 1)


class ProfileDetailTest(TestCase):

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
