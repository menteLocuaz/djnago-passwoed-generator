from django.shortcuts import render
import random

# Create your views here.
def about(request):
    context = {}
    return render(request, "generator/about.html", context)


def home(request):
    context = {}
    return render(request, "generator/home.html", context)


def password(request):
    charter = list("abcdefghyabcdefghijklmnñopqrstuvwxyz")
    generate_password = ""

    valor = int(request.GET.get("length"))
    if request.GET.get("uppercase"):
        charter.extend(list("ABCDEFGHYABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
    if request.GET.get("special"):
        charter.extend(list('!"·$%&/()=?¿*^¨_:'))
    if request.GET.get("number"):
        charter.extend(list("01234567890123456789"))

    for x in range(valor):
        generate_password += random.choice(charter)
    context = {"password": generate_password}
    return render(request, "generator/password.html", context)
