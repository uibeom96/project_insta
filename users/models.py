from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nick_name = models.CharField(max_length=10)


    class Meta:
        db_table = "users"

    def __str__(self):
        self.username
