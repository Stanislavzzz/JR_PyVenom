from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главное страница."""
    return HttpResponse("<h1>Hello, world.</h1><hr><p>Наш блог.</p>")


def about(request):
    """Страница о нас."""
    return HttpResponse("<h1>About us.</h1><hr><p>Страница о нас.</p> 'SELECT * FROM post'")
