from django.shortcuts import render
from .models import Category, Book, Orders
from .serializers import CategorySerializer,  BookSerializer,  OrdersSerializer
# Create your views here.
from rest_framework import generics, filters


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class OrdersListView(generics.ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['book']
