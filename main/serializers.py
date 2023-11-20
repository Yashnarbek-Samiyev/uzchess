from rest_framework import serializers
from .models import Country, Main, Languages, Player1, Player2, Reyting, Plays, Notice


class CountrySeializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = '__all__'


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class Player1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Player1
        fields = '__all__'


class Player2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Player2
        fields = '__all__'


class ReytingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reyting
        fields = '__all__'


class PlaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plays
        fields = '__all__'


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = '__all__'
