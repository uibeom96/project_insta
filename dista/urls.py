from django.urls import path
from dista import views


app_name = "dista"

urlpatterns = [
    path("", views.dista_main, name="dista_main")
]