from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.bug_list, name='bug_list'),
    path('features/', views.feature_list, name='feature_list'),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='feature_detail'),
]
