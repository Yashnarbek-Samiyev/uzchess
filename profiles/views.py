from django.shortcuts import render
from rest_framework import viewsets
from .models import Category, User, PurchasedCourses, UserOrders, Saved, SavedCourses, SavedBooks, UserSettings
from .serializers import CategorySerializer, UserSerializer, PurchasedCoursesSerializer, UserOrdersSerializer, SavedSerializer, SavedCoursesSerializer, SavedBooksSerializer, UserSettingsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class ProfileCategoryList(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserListView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PurchasedCoursesListView(viewsets.ModelViewSet):
    queryset = PurchasedCourses.objects.all()
    serializer_class = PurchasedCoursesSerializer


class UserOrdersListView(viewsets.ModelViewSet):
    queryset = UserOrders.objects.all()
    serializer_class = UserOrdersSerializer


class SavedListView(viewsets.ModelViewSet):
    queryset = Saved.objects.all()
    serializer_class = SavedSerializer


class SavedCoursesListView(viewsets.ModelViewSet):
    queryset = SavedCourses.objects.all()
    serializer_class = SavedCoursesSerializer


class SavedBooksListView(viewsets.ModelViewSet):
    queryset = SavedBooks.objects.all()
    serializer_class = SavedBooksSerializer
    field_backends = ['django_filters.rest_framework.DjangoFilterBackend',
                      'rest_framework.filters.SearchFilter', 'rest_framework.filters.OrderingFilter']

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class UserSettingsListView(viewsets.ModelViewSet):
    queryset = UserSettings.objects.all()
    serializer_class = UserSettingsSerializer
