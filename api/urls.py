from django.urls import path
from .views import BeachListCreate, BeachDetail, CommentSectionListCreate, CommentSectionDetail, GeneralCommentSectionListCreate, GeneralCommentSectionDetail, CommentListCreate, CommentDetail, ReportListCreate, ReportDetail, SourceListCreate, SourceDetail

app_name = 'api'
urlpatterns = [
    path('beaches/', BeachListCreate.as_view(), name='beach-list-create'),
    path('beaches/<int:pk>/', BeachDetail.as_view(), name='beach-detail'),
    
    path('comment-sections/', CommentSectionListCreate.as_view(), name='comment-section-list-create'),
    path('comment-sections/<int:pk>/', CommentSectionDetail.as_view(), name='comment-section-detail'),
    
    path('general-comment-sections/', GeneralCommentSectionListCreate.as_view(), name='general-comment-section-list-create'),
    path('general-comment-sections/<int:pk>/', GeneralCommentSectionDetail.as_view(), name='general-comment-section-detail'),
    
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    
    path('reports/', ReportListCreate.as_view(), name='report-list-create'),
    path('reports/<int:pk>/', ReportDetail.as_view(), name='report-detail'),
    
    path('sources/', SourceListCreate.as_view(), name='source-list-create'),
    path('sources/<int:pk>/', SourceDetail.as_view(), name='source-detail'),
]
