from django.shortcuts import render
from rest_framework import generics, filters
from .models import Main, Languages, Country, Player1, Player2, Reyting, Plays, Notice
from .serializers import CountrySeializer, MainSerializer, LanguagesSerializer, Player1Serializer, Player2Serializer, ReytingSerializer, PlaysSerializer, NoticeSerializer


# Create your views here.
class MainListView(generics.ListAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class LanguagesListView(generics.ListAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer


class Player1ListView(generics.ListAPIView):
    queryset = Player1.objects.all()
    serializer_class = Player1Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class Player2ListView(generics.ListAPIView):
    queryset = Player2.objects.all()
    serializer_class = Player2Serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ReytingListView(generics.ListAPIView):
    queryset = Reyting.objects.all()
    serializer_class = ReytingSerializer


class NoticeListView(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer


class CountryListView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySeializer


class PlaysListView(generics.ListAPIView):
    queryset = Plays.objects.all()
    serializer_class = PlaysSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['country__name', 'players__name']
