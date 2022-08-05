"""Performs conversion of data to required structure."""

from rest_framework import serializers
from book_api.models import Book
from django.forms import ValidationError


class BookSerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "number_of_pages",
                  "publish_date", "quantity", "description"]
        read_only_fields = ["id"]

    def validate_title(self, value):
        if value == "Diet Coke":
            raise ValidationError("No Diet Coke Please.")
        return value

    def validate(self, data):
        if data["number_of_pages"] < 100:
            raise ValidationError("Too few pages. Big Books only.")
        return data

    def get_description(self, data):
        return f"This book is called {str(data)} and it is {str(data.number_of_pages)} pages long."
