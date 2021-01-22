from django.shortcuts import render

from django.http import HttpResponse
#created one view called index, each view takes in at least one argument(a HttpRequest object)
def index(request):
    return HttpResponse("Rango says hey there partner!")
