from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
import Book.models as mo
from Book.forms import BookForm


def books(request):
    if request.user.is_authenticated:
        books = mo.Book.objects.all()
        return render(request, 'books_main.html', context={'books': books})
    else:
        return HttpResponse(f"<a href='/admin/login'>Login</a")

def get_book(request, id):
    book = mo.Book.objects.get(id=id)
    return render(request, 'book.html', context={'book': book})

def create_book(request):
    if request.POST:
        form = BookForm(request.POST)
        form.is_valid()
        form.save()
    return render(request, 'create_book.html', context={'form': BookForm()})