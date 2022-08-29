from urllib import request
from django.http import HttpResponse


def teste(request):
    return HttpResponse("E o resto você já sabe")

def teste2(request):
    return HttpResponse("E o resto você já sabe 2.0")