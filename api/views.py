from rest_framework import generics
from core.models import Beach, Comment, Report, Map, EducationalContent
from .serializers import BeachSerializer, CommentSerializer, ReportSerializer, MapSerializer, EducationalContentSerializer

class BeachListCreate(generics.ListCreateAPIView):
    queryset = Beach.objects.all()
    serializer_class = BeachSerializer

class BeachDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BeachSerializer
    lookup_field = 'urlName'  # Use 'urlName' instead of 'pk'

    def get_queryset(self):
        return Beach.objects.all()  # Retrieve all beach objects, then filter by 'urlName'

class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    # Override the get_queryset method to filter based on the beach name
    def get_queryset(self):
        beach_id = self.kwargs['beach_id']
        return Comment.objects.filter(beach_id=beach_id)

    def perform_create(self, serializer):
        beach_id = self.kwargs['beach_id']
        serializer.save(beach_id=beach_id)

class ReportListCreate(generics.ListCreateAPIView):
    serializer_class = ReportSerializer
    
    def get_queryset(self):
        beach_id = self.kwargs['beach_id']
        return Report.objects.filter(beach__id=beach_id)
    
    def perform_create(self, serializer):
        beach_id = self.kwargs['beach_id']
        serializer.save(beach_id=beach_id)

class MapListCreate(generics.ListCreateAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer

class MapDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Map.objects.all()
    serializer_class = MapSerializer    

class EducationalContentListCreate(generics.ListCreateAPIView):
    queryset = EducationalContent.objects.all()
    serializer_class = EducationalContentSerializer