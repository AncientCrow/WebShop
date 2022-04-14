
from django.test import TestCase

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from web_shop.settings import BASE_DIR
from app_registration import forms

class RegistrationFormTest(TestCase):

    def test_username_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["username"].label == "Nickname")

    def test_first_name_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["first_name"].label == "First name")

    def test_second_name_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["last_name"].label == "Last name")

    def test_password_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["password1"].label == "Password")

    def test_confirm_password_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["password2"].label == "Password confirm")

    def test_email_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["email"].label == "Email")

    def test_icon_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["profile_icon"].label == "Profile icon")

    def test_form_values(self):
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
            "email": "test@test.com",
        }
        form = forms.RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())


class LoginFormTest(TestCase):

    def test_username_label(self):
        form = forms.LoginForm()
        self.assertTrue(form.fields["username"].label == "Nickname" or None)

    def test_passport_label(self):
        form = forms.LoginForm()
        self.assertTrue(form.fields["password"].label == "Password" or None)

    def test_form_values(self):
        User.objects.create_user(
            username="test",
            email="test@test.ru",
            password="123qwe!@#",
        )
        form_data = {
            "username": "test",
            "password": "123qwe!@#"
        }
        form = forms.LoginForm(data=form_data)
        self.assertTrue(form.is_valid())
