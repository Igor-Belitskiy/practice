from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import User


def index(request):
    if request.method == "POST":
        user = User(request.POST)
        if user.is_valid():
            name = user.cleaned_data["username"]#Находится в классе django AbstractUser username

            return HttpResponse("<h2>Hello, {0}</h2>".format(name))
        else:
            return HttpResponse("Invalid data")
    else:
        user = User()
        return render(request, "index.html", {"form": user})