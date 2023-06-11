from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib import messages


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


def quienes_somos(request):
    return render(request, "home/quienes_somos.html")


def contacto(request):
    return render(request, "home/contacto.html")
