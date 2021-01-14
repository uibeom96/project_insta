from django.db import models
from base.models import BaseModel
from django.conf import settings


class Post(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Photo/%Y-%m-%d")
    hash_tag = models.CharField(max_length=30)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True) 
    dis_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="dis_likes", blank=True) 
    follower = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers" ,blank=True)
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings", blank=True)

    class Meta:
        ordering = ("-created", )
        db_table = "post"
        verbose_name = "작성된 포스트"
        verbose_name_plural = "모든 포스트"

    def __str__(self):
        return str(self.author)+"의 글"

class Comment(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")

    class Meta:
        ordering = ("-created", )
        db_table = "comment"
        verbose_name = "작성된 댓글"
        verbose_name_plural = "모든 댓글"

    def __str__(self):
        return str(self.author)+"님의 댓글"