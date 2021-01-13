from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dista_main(request):
    return render(request, "dista/dista_main.html")

