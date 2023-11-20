from django.shortcuts import render
from .models import News, Rules
from rest_framework import generics, filters
from .serializers import NewsSerializer, RulesSerializer

# Create your views here


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class RulesListView(generics.ListAPIView):
    queryset = Rules.objects.all()
    serializer_class = RulesSerializer
