from django.urls import path
from accounts import views

app_naem = "accounts"

urlpatterns = [
    path("signup/", views.accounts_signup, name="signup"),
]