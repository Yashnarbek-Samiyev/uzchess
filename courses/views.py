from rest_framework import generics, filters
from .models import Category, Languages, Filter, Course, Lesson, Comments, Certificate, Report
from .serializers import CategorySerializer, LanguagesSerializer, FilterSerializer, CourseSerializer, LessonSerializer, CommentsSerializer, CerificateSerializer, ReportSerializer

# Create your views here.


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LanguagesListView(generics.ListAPIView):
    queryset = Languages.objects.all()
    serializer_class = LanguagesSerializer


class FilterListView(generics.ListAPIView):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer


class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class LessonListView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class CommentsListView(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CertificateListView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CerificateSerializer


class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
