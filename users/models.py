from base.models import BaseModel
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser, BaseModel):
    nick_name = models.CharField(max_length=10)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings", blank=True)


    class Meta:
        db_table = "users"
        verbose_name = "회원"
        verbose_name_plural = "회원정보"

    def __str__(self):
        return self.username
