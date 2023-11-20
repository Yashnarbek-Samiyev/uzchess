from rest_framework import serializers
from .models import Category, Book,  Orders


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = "__all__"


class OrdersSerializer(serializers.Serializer):
    class Meta:
        model = Orders
        fields = "__all__"
