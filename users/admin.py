from django.contrib import admin
from users.models import User
from django.contrib.auth.models import Group

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username")
    list_display_links = ("username", )

admin.site.unregister(Group) # Admin페이지의 GROUP삭제