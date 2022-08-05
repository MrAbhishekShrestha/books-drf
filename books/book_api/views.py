"""Books Views."""
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET'])
def book_list(request):
    books = Book.objects.all()  # complex data
    serializer = BookSerializer(books, many=True)  # Json data
    return Response(serializer.data)
