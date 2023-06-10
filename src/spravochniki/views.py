from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from . import models

def home_page(request):
    books = models.Book.objects.filter(pk__lt = 15)
    return render(
        request,
        template_name="spravochniki/home-page.html",
        context={'objects': books}
    )

def view_book(request, pk):
    book = models.Book.objects.get(pk=int(pk))    
    return render(
        request,
        template_name="spravochniki/view-book.html",
        context={'object': book}
    )

def delete_book(request, pk):
    models.Book.objects.get(pk=int(pk)).delete()
    return HttpResponse(f"object {pk} has been deleted!")

# Create your views here.
