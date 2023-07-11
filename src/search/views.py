from django.shortcuts import render
from spravochniki import models
from django.db.models import Q

def search_view(request):
    res = []
    q = None
    if request.method == "POST":        
        q = request.POST.get("q")
        books = models.Book.objects.filter(Q(name__contains=q))
        autors = models.Autor.objects.filter(Q(name__contains=q))
        
        for obj in books:
            res.append((obj.name, obj.get_search_url()))
        for obj in books:
            res.append((obj.name, obj.get_search_url()))
    context = {"results": res, "q": q}    
    return render(
        request, 
        template_name="search/search_result.html",
        context=context)

# Create your views here.
