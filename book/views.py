import json
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from book.models import Book

# Create your views here.
def home(request):
    context = {}
    return render(request, 'index.html', context)


def apiBooks(request):
    all_books_obj = Book.objects.all()
    all_books_dict = [ model_to_dict(book) for book in all_books_obj ]
    all_books_dict = { 'books': all_books_dict } 
    return JsonResponse(all_books_dict, safe=False)

@csrf_exempt
def apiBooksId(request, id):
    book_dict = ""
    if request.method == 'POST':       
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = float(request.POST.get('price'))
        iventory = int(request.POST.get('iventory'))
        new_book_obj = Book(title=title, author=author, price=round(price,2), iventory=iventory)
        try:
            new_book_obj.save()
            book_dict = model_to_dict(new_book_obj)
        except IntegrityError:
            return JsonResponse({'error':'true','message':'required field missing'},status=400)
    if request.method == 'GET':    
        book_obj = Book.objects.get(pk=id)
        book_dict = model_to_dict(book_obj)
        book_dict = { 'book': book_dict } 
    return JsonResponse(book_dict, safe=False, status=201)
  