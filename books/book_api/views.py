"""Books Views."""
from book_api.models import Book
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class BookList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookCreate(APIView):

    def post(self, request):
        """POST request handler to add new book."""
        serializer = BookSerializer(
            data=request.data)  # converts json -> complex data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleBook(APIView):

    def get_book_by_pk(self, pk):
        try:
            book = Book.objects.get(pk=pk)
            return book, True
        except:
            return Response({
                'error': 'Book does not exist'
            }, status=status.HTTP_404_NOT_FOUND), False

    def get(self, request, pk):
        book, success = self.get_book_by_pk(pk)
        if not success:
            return book
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        book, success = self.get_book_by_pk(pk)
        if not success:
            return book
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book, success = self.get_book_by_pk(pk)
        if not success:
            return book
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
