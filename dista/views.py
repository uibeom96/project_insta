from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dista.models import Post


@login_required
def dista_main(request):
    post_list = Post.objects.all()
    return render(request, "dista/dista_main.html", {"post_list": post_list})

