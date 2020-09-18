from django.contrib import admin
from Book.models import Book

class BookAdmin(admin.ModelAdmin):
    fields = ('titele', 'description', 'author', 'author_name')
    search_fields = 'titele',
    list_display = 'titele', 'short_description', 'author'
    list_filter = 'author',
admin.site.register(Book, BookAdmin)