from django.test import TestCase
from .. import forms
from datetime import datetime
from django.contrib.auth.models import User


class RegistrationFormTest(TestCase):

    def test_username_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["username"].label == "Nickname" or None)

    def test_first_name_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["first_name"].label == "First name" or None)

    def test_second_name_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["last_name"].label == "Last name" or None)

    def test_password_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["password1"].label == "Password" or None)

    def test_confirm_password_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["password2"].label == "Password confirm" or None)

    def test_email_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["email"].label == "Email" or None)

    def test_date_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["date"].label == "Birthday" or None)

    def test_phone_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["phone"].label == "Phone number" or None)

    def test_city_label(self):
        form = forms.RegistrationForm()
        self.assertTrue(form.fields["city"].label == "Your city" or None)

    def test_form_values(self):
        form_data = {
            "username": "test",
            "first_name": "Bob",
            "last_name": "Ivanov",
            "password1": "123qwe!@#",
            "password2": "123qwe!@#",
            "email": "test@test.com",
            "date": datetime.now(),
            "phone": "+79042222222",
            "city": "Айкадыр"
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
        User.objects.create_user(username="test", email="test@test.ru", password="123qwe!@#")
        form_data = {
            "username": "test",
            "password": "123qwe!@#"
        }
        form = forms.LoginForm(data=form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())
