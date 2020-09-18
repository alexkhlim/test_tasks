from django.urls import path
from Book.views import (books,
                        get_book,
                        create_book)



urlpatterns = [
    path('books/', books),
    path('books/<id>', get_book, name='books'),
    path('create/', create_book)
]