from rest_framework import serializers
from .models import News, Rules


class NewsSerializer(serializers.Serializer):
    class Meta:
        model = News
        fields = '__all__'


class RulesSerializer(serializers.Serializer):
    class Meta:
        model = Rules
        fields = '__all__'
