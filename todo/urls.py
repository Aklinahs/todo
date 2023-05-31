from django.urls import path, include
from . import views

urlpatterns = [
    path('addTask', views.addTask, name='addTask'),
    path('mark_as_done/<int:task_id>', views.mark_as_done, name='mark_as_done'),
    path('mark_as_undone/<int:task_id>', views.mark_as_undone, name='mark_as_undone'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('delete/<int:task_id>', views.delete, name='delete'),
]
