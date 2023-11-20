from django.urls import path
from .views import CategoryListView, LanguagesListView, FilterListView, CourseListView, LessonListView, CommentsListView, CertificateListView, ReportListView

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('languages/', LanguagesListView.as_view()),
    path('filter/', FilterListView.as_view()),
    path('course/', CourseListView.as_view()),
    path('lesson/', LessonListView.as_view()),
    path('comments/', CommentsListView.as_view()),
    path('certificate/', CertificateListView.as_view()),
    path('report/', ReportListView.as_view(),)
]
