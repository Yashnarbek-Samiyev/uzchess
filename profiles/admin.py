from django.contrib import admin
from .models import Category, User, PurchasedCourses, UserOrders, Saved, SavedCourses, SavedBooks, UserSettings
# Register your models here.
admin.site.register(Category)
admin.site.register(User)
admin.site.register(PurchasedCourses)
admin.site.register(UserOrders)
admin.site.register(Saved)
admin.site.register(SavedCourses)
admin.site.register(SavedBooks)
admin.site.register(UserSettings)
