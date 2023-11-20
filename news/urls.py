from django.urls import path, include
from .views import NewsListView, RulesListView

urlpatterns = [
    path('news/', NewsListView.as_view()),
    path('rules/', RulesListView.as_view()),
]
