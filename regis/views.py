from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.core import serializers


def index(request):
    if request.method == "POST":
        user = User(request.POST)


        if user.is_valid():
            name = user.cleaned_data["username"]

            user = serializers.serialize('xml', user.objects.all())

            user.set_password(user.password)
            user.save()

            return HttpResponse("<h2>Данные правильные, {0}</h2>".format(name))
        else:
            return HttpResponse("Ошибка ввода")
    else:
        user = User()
        return render(request, "index.html", {"form": user})