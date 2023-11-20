from rest_framework import serializers
from .models import Category, User, PurchasedCourses, UserOrders, Saved, SavedCourses, SavedBooks, UserSettings


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class PurchasedCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchasedCourses
        fields = "__all__"


class UserOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrders
        fields = "__all__"


class SavedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saved
        fields = "__all__"


class SavedCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedCourses
        fields = "__all__"


class SavedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedBooks
        fields = "__all__"


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSettings
        fields = "__all__"
