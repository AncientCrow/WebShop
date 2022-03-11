from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .. import models


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
    def test_url_exist(self):
        response = self.client.get("/user/1/", )
        self.assertEqual(response.status_code, 200)

    def test_url_exist_by_name(self):
        response = self.client.get(reverse("user_detail", kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_use_valid_template(self):
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
