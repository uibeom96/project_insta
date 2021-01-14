from django.contrib import admin
from dista.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "author")

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author")
