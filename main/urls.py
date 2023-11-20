from django.urls import path
from .views import MainListView, LanguagesListView, CountryListView, Player1ListView, Player2ListView, ReytingListView, PlaysListView, NoticeListView

urlpatterns = [
    path('main/', MainListView.as_view()),
    path('languages/', LanguagesListView.as_view()),
    path('country/', CountryListView.as_view()),
    path('player1/', Player1ListView.as_view()),
    path('player2/', Player2ListView.as_view()),
    path('reyting/', ReytingListView.as_view()),
    path('plays/', PlaysListView.as_view()),
    path('notice/', NoticeListView.as_view()),
]
