from django.urls import path
from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('another_page/', views.another_page, name='another_page'),
]
