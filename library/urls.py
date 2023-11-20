from django.urls import path
from .views import CategoryListView, BookListView, OrdersListView


urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('book/', BookListView.as_view()),
    path('orders/', OrdersListView.as_view()),
]
