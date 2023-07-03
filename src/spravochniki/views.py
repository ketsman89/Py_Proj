from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from random import randint
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import models
from . import forms






class BookView(generic.DetailView):
    model = models.Book

class BookCreateView(generic.CreateView):
    model = models.Book
    template_name = "spravochniki/book_form.html"
    fields = [
            "name", 
            "autor", 
            "genre", 
            "serie", 
            "publisher",
            "picture",
            "price",
            "year",
            "pages",
            "cover",
            "format",
            "isbn",
            "age",
            "numbers",
            "availability",
            "rating",
            "weight",
            "created",
            "updated",
        ]
    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
    
class BookUpdateView(generic.UpdateView):
    model = models.Book
    template_name = "spravochniki/book_form.html"
    fields = [
            "name", 
            "autor", 
            "genre", 
            "serie", 
            "publisher",
            "picture",
            "price",
            "year",
            "pages",
            "cover",
            "format",
            "isbn",
            "age",
            "numbers",
            "availability",
            "rating",
            "weight",
            "created",
            "updated",
        ]
    def form_valid(self, form):
        if form.has_changed():
            if 'picture' in form.changed_data:
                print(form.changed_data)
        return super().form_valid(form)

    def get_success_url(self) -> str:
        self.object.picture_resizer()
        return super().get_success_url()
    # success_url = "/added" сделан get_absolute_url в models

class BookDeleteView(generic.DeleteView):
    model = models.Book
    template_name = "spravochniki/delete-book.html"
    success_url = "/" # здесь необходимо указать редирект, так как объект удаляется

class BookListView(LoginRequiredMixin, generic.ListView):
    model = models.Book
    paginate_by = 20
    # login_url = reverse_lazy("staff:login")

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

def add_book(request):    
    if request.method == "GET":
        form = forms.BookModelForm()
        return render(
            request,
            template_name="spravochniki/add-book.html",
            context={            
            "greeting": "Add a new Book!",
            "form": form
            }
        )
    else:        
        book_form = forms.BookModelForm(request.POST)
        if book_form.is_valid():        
            new_book = book_form.save()
            return HttpResponseRedirect("/added")
        else:
            return render(
            request,
            template_name="spravochniki/add-book.html",
            context={            
            "greeting": "Add a new Book!",
            "form": book_form
            })

    

def update_book(request, pk):
    autors = models.Autor.objects.all()
    genres = models.Genre.objects.all()
    series = models.Serie.objects.all()
    publishers = models.Publisher.objects.all()
    if request.method == "GET":
        book = models.Book.objects.get(pk=pk)
        return render(
            request,
            template_name="spravochniki/update-book.html",
            context={
                "object": book,
                "autors": autors,
                "genres": genres,
                "series": series,
                "publishers": publishers,
                "greeting": "Edit the Book!"
            }
        )
    else:
        book_name = request.POST.get("book_name")
        autor_id = request.POST.get("autor")
        autor = models.Autor.objects.get(pk=int(autor_id))
        genre_id = request.POST.get("genre")
        genre = models.Genre.objects.get(pk=int(genre_id))
        serie_id = request.POST.get("serie")
        serie = models.Serie.objects.get(pk=int(serie_id))
        publisher_id = request.POST.get("publisher")
        publisher = models.Publisher.objects.get(pk=int(publisher_id))    
        print(book_name)
        new_book = models.Book.objects.update(
            name=book_name,
            autor=autor,
            genre=genre,
            serie=serie,
            publisher=publisher
        )
        return HttpResponseRedirect("/added")


def succes_page(request):
    return render(
        request,
        template_name="spravochniki/added-successfully.html",
        context={"message": f"The object was created!"}
    )

def send_email(request):
    if request.method == "GET":
        form = forms.ContactForm()
        return render(
            request,
            template_name="spravochniki/send-email.html",
            context={"form": form}
        )
    else:        
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            # sent the data
            form.send_email()
            return HttpResponseRedirect("/added")
        else:
            return render(
            request,
            template_name="spravochniki/send-email.html",
            context={"form": form})
    
def book_det_API(request, pk):
    book = models.Book.objects.get(pk=pk)    
    return JsonResponse({"picture": book.picture, "name": book.name})

# Create your views here.
