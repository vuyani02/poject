from rest_framework import generics
from core.models import Beach, CommentSection, GeneralCommentSection, Comment, Report, Source
from .serializers import BeachSerializer, CommentSectionSerializer, GeneralCommentSectionSerializer, CommentSerializer, ReportSerializer, SourceSerializer

class BeachListCreate(generics.ListCreateAPIView):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer

class BeachDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer

class CommentSectionListCreate(generics.ListCreateAPIView):
    queryset = CommentSection.objects.all()
    serializer_class = CommentSectionSerializer

class CommentSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentSection.objects.all()
    serializer_class = CommentSectionSerializer

class GeneralCommentSectionListCreate(generics.ListCreateAPIView):
    queryset = GeneralCommentSection.objects.all()
    serializer_class = GeneralCommentSectionSerializer

class GeneralCommentSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralCommentSection.objects.all()
    serializer_class = GeneralCommentSectionSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ReportListCreate(generics.ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class SourceListCreate(generics.ListCreateAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer

class SourceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
