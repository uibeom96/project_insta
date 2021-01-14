from django.shortcuts import render, redirect
from accounts.forms import UserForm
from users.models import User

def accounts_signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            del(form.cleaned_data["password2"])
            User.objects.create_user(**form.cleaned_data)
            return redirect("dista:dista_main")
    else:
        form = UserForm()
    return render(request, "accounts/signup.html", {"form": form})