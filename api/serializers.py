from rest_framework import serializers
from core.models import Beach, CommentSection, GeneralCommentSection, Comment, Report, Source, Map

class BeachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beach
        fields = '__all__'

class CommentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentSection
        fields = '__all__'

class GeneralCommentSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCommentSection
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = '__all__'

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'
