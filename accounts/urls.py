from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_view

app_naem = "accounts"

urlpatterns = [
    path("signup/", views.accounts_signup, name="signup"),
    path("logins/", auth_view.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
]