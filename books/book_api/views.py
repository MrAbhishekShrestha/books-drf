"""Books Views."""
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET'])
def book_list(request):
    """GET request handler to return all books."""
    books = Book.objects.all()  # complex data
    serializer = BookSerializer(books, many=True)  # Json data
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def book_create(request):
    """POST request handler to add new book."""
    serializer = BookSerializer(
        data=request.data)  # converts json -> complex data
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def book(request, pk):
    """Handles GET, PUT, DELETE operations for a single book, based on the pk."""
    try:
        book = Book.objects.get(pk=pk)
    except:
        return Response({
            'error': 'Book does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = BookSerializer(book, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
