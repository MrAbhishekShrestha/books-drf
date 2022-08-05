"""Performs conversion of data to required structure."""

from rest_framework import serializers
from book_api.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "number_of_pages", "publish_date", "quantity"]
        read_only_fields = ["id"]
