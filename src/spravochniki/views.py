from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from . import models

def home_page(request):
    books = models.Book.objects.filter(pk__lt = 200)
    html = "<ul>"
    for book in books:
        html += f"<li>{book.pk} Book {book.name}</li>"
    html += "</ul>"
    return HttpResponse(html)
# Create your views here.
