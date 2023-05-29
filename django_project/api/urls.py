from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.api_overview, name='api-overview'),
    path('tasks/', views.task_list, name='task-list'),
    path('tasks/<str:pk>/', views.task_detail, name='task-detail'),
    path('tasks/', views.task_create, name='task-create'),
    path('tasks/<str:pk>/', views.task_update, name='task-update')
]
