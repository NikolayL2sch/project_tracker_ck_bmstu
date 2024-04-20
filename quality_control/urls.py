from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.BugsListView.as_view(), name='bug_list'),
    path('bugs/add_bug', views.BugReportCreateView.as_view(), name='create_bug_report'),
    path('features/add_feature', views.FeatureRequestCreateView.as_view(), name='add_feature'),
    path('features/', views.FeatureListView.as_view(), name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
    path('bugs/<int:bug_id>/update/', views.update_bug_report, name='update_bug_report'),
    path('features/<int:feature_id>/update/', views.update_feature_request, name='update_feature_request'),
]
