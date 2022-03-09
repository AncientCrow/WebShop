from django.urls import path
from . import views

urlpatterns = [
    path("registration/", views.RegistrationPage.as_view(), name="registration"),
    path("login/", views.LoginPage.as_view(), name="login"),
    path("logout/", views.Logout.as_view(), name="logout"),
    path("user/<int:pk>/", views.ProfileDetail.as_view(), name="user_detail"),
    path("user/<int:pk>/edit/", views.UserEdit.as_view(), name="user_edit")
]
