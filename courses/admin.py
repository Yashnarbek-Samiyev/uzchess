from django.contrib import admin
from .models import Category, Filter, Course, Lesson, Comments, Certificate, Report

# Register your models here.
admin.site.register(Category)
admin.site.register(Filter)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Comments)
admin.site.register(Certificate)
admin.site.register(Report)
