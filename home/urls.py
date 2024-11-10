from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.tasks, name='tasks'),
    
    # Task management paths
    path('tasks/create/', views.create_task, name='create_task'),         # Create new task
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'), # Edit existing task
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'), # Delete task
    # path('tasks/', views.task_list, name='task_list'),
    path('tasks/toggle-status/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),
    ]
