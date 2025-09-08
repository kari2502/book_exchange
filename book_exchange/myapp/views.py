from django.shortcuts import render, HttpResponse
from .models import TodoItem, Book


# Create your views here.
def home(request):
    return render(request, "home.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})


def books(request):
    all_books = Book.objects.all()
    print(all_books)
    return render(request, "books.html", {"Books": all_books})
