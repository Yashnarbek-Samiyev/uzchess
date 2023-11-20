from django.urls import path
from . import views

urlpatterns = [
    path('profilecategory/', views.ProfileCategoryList.as_view()),
    path('user/', views.UserListView.as_view()),
    path('purchasedcourses/', views.PurchasedCoursesListView.as_view()),
    path('userorders/', views.UserOrdersListView.as_view()),
    path('saved/', views.SavedListView.as_view()),
    path('savedcourses/', views.SavedCoursesListView.as_view()),
    path('savedbooks/', views.SavedBooksListView.as_view()),
    path('usersettings/', views.UserSettingsListView.as_view()),

]
