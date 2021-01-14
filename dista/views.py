from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dista.models import Post
from dista.forms import PostForm


@login_required
def dista_main(request):
    post_list = Post.objects.filter(is_deleted=False)
    return render(request, "dista/dista_main.html", {"post_list": post_list})


def dista_add(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False) 
            data.author = request.user
            data.save()
            return redirect("dista:dista_main")
    else:
        form = PostForm()
    return render(request, "dista/dista_add.html", {"form": form})


def dista_update(request, pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            data = form.save(commit=False)
            data.author = request.user
            data.save()
            return redirect("dista:dista_main")
    else:
        form = PostForm(instance=post)
    return render(request, "dista/dista_update.html", {"post": post, "form": form})


def dista_delete(request, pk):
    post = get_object_or_404(Post, id=pk)
    post.delete()
    return redirect("dista:dista_main")



def dista_detail(request):
    pass