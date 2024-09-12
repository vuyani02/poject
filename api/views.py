from rest_framework import generics
from core.models import Beach, CommentSection, Comment, Report, Source, Map
from .serializers import BeachSerializer, CommentSectionSerializer, CommentSerializer, ReportSerializer, SourceSerializer, MapSerializer
from rest_framework.response import Response
from rest_framework import status

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

'''
class GeneralCommentSectionListCreate(generics.ListCreateAPIView):
    queryset = GeneralCommentSection.objects.all()
    serializer_class = GeneralCommentSectionSerializer

class GeneralCommentSectionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralCommentSection.objects.all()
    serializer_class = GeneralCommentSectionSerializer'''

class CommentListCreate(generics.ListCreateAPIView):
    #queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        beach_id = self.kwargs['beach_id']
        return Comment.objects.filter(beach__id=beach_id)
    
    def perform_create(self, serializer):
        beach_id = self.kwargs['beach_id']
        serializer.save(beach_id=beach_id)


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

class MapListCreate(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer    
