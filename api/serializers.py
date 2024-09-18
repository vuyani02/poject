from rest_framework import serializers
from core.models import Beach, Comment, Report, Map, EducationalContent

class BeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beach
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'

class EducationalContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalContent
        fields = '__all__'        
