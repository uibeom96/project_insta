from django.urls import path
from dista import views


app_name = "dista"

urlpatterns = [
    path("", views.dista_main, name="dista_main"),
    path("add/", views.dista_add, name="dista_add"),
    path("update/<int:pk>", views.dista_update, name="dista_update"),
    path("delete/<int:pk>", views.dista_delete, name="dista_delete"),    
    path("detail/<int:pk>", views.dista_detail, name="desta_detail"),
]