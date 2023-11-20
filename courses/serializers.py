from rest_framework import serializers
from .models import Category, Languages, Filter, Course, Lesson, Comments, Certificate, Report


class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = "__all__"


class LanguagesSerializer(serializers.Serializer):
    class Meta:
        model = Languages
        fields = "__all__"


class FilterSerializer(serializers.Serializer):
    class Meta:
        model = Filter
        fields = "__all__"


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = "__all__"


class LessonSerializer(serializers.Serializer):
    class Meta:
        model = Lesson
        fields = "__all__"


class CommentsSerializer(serializers.Serializer):
    class Meta:
        model = Comments
        fields = "__all__"


class CerificateSerializer(serializers.Serializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class ReportSerializer(serializers.Serializer):
    class Meta:
        model = Report
        fields = "__all__"
