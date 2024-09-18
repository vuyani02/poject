from django.urls import path
from .views import BeachListCreate, BeachDetail, CommentListCreate, ReportListCreate, MapListCreate, MapDetail, EducationalContentListCreate

app_name = 'api'
urlpatterns = [
    path('beaches/', BeachListCreate.as_view(), name='beach-list-create'),
    path('beaches/<str:urlName>/', BeachDetail.as_view(), name='beach-detail'),
    
    path('beaches/<int:beach_id>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    
    path('beaches/<int:beach_id>/reports/', ReportListCreate.as_view(), name='report-list-create'),

    path('map/', MapListCreate.as_view(), name='map-list-create'),
    path('map/<int:pk>/', MapDetail.as_view(), name='map-detail'),

    path('EducationalContent/', EducationalContentListCreate.as_view(), name='EducationalContent-list-create'),
    
]
