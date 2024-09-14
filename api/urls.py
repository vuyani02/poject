from django.urls import path
from .views import BeachListCreate, BeachDetail, CommentSectionListCreate, CommentSectionDetail, CommentListCreate, CommentDetail, ReportListCreate, SourceListCreate, SourceDetail, MapListCreate, MapDetail

app_name = 'api'
urlpatterns = [
    path('beaches/', BeachListCreate.as_view(), name='beach-list-create'),
    path('beaches/<str:urlName>/', BeachDetail.as_view(), name='beach-detail'),
    
    path('comment-sections/', CommentSectionListCreate.as_view(), name='comment-section-list-create'),
    path('comment-sections/<int:pk>/', CommentSectionDetail.as_view(), name='comment-section-detail'),
    
    path('beaches/<int:beach_id>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    
    path('beaches/<int:beach_id>/reports/', ReportListCreate.as_view(), name='report-list-create'),
    #path('reports/<int:pk>/', ReportDetail.as_view(), name='report-detail'),
    
    path('sources/', SourceListCreate.as_view(), name='source-list-create'),
    path('sources/<int:pk>/', SourceDetail.as_view(), name='source-detail'),

    path('map/', MapListCreate.as_view(), name='map-list-create'),
    path('map/<int:pk>/', MapDetail.as_view(), name='map-detail'),
    
]

'''
    path('general-comment-sections/', GeneralCommentSectionListCreate.as_view(), name='general-comment-section-list-create'),
    path('general-comment-sections/<int:pk>/', GeneralCommentSectionDetail.as_view(), name='general-comment-section-detail'),'''
