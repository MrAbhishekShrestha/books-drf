"""Books Views."""
from book_api.models import Book
from django.http import JsonResponse

# Create your views here.


def book_list(request):
    books = Book.objects.all()  # complex data
    books_python = list(books.values())  # python ds
    return JsonResponse({
        'books': books_python
    })
