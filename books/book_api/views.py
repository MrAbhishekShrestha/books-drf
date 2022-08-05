"""Books Views."""
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def book_list(request):
    """GET request handler to return all books."""
    books = Book.objects.all()  # complex data
    serializer = BookSerializer(books, many=True)  # Json data
    return Response(serializer.data)


@api_view(['POST'])
def book_create(request):
    """POST request handler to add new book."""
    serializer = BookSerializer(
        data=request.data)  # converts json -> complex data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    """Handles GET, PUT, DELETE operations for a single book, based on the pk."""
    if request.method == 'GET':
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
