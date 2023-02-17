import json
from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import render
from django.forms.models import model_to_dict

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


def apiBooksId(request, id):
    request_body = QueryDict(request.body)
    print(request_body)
    request = request_body.get('title')
    print(request)
    book_obj = Book.objects.get(pk=id)
    book_dict = model_to_dict(book_obj)
    book_dict = { 'book': book_dict } 
    return JsonResponse(book_dict, safe=False)
  