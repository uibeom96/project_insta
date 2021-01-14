from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from dista.models import Post, Comment
from users.models import User
from dista.forms import PostForm, CommentForm


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



def dista_detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    comment_list = Comment.objects.filter(post=post, is_deleted=False)
    if request.method == "POST":
        data = Comment.objects.create(
            post=post,
            author=request.user,
            comment=request.POST.get("comment"))
        data.save()
    return render(request, "dista/dista_detail.html", {"post": post, "comment_list": comment_list})


def dista_profile(request, pk):
    user = get_object_or_404(User, id=pk)
    posts = Post.objects.filter(author=user, is_deleted=False)
    print(posts)
    return render(request, "dista/dista_profile.html", {"user": user, "posts": posts})

