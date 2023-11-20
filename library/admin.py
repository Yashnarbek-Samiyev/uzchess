from django.contrib import admin
from .models import Category, Book, Orders
# Register your models here.

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Orders)
