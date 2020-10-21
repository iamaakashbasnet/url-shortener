from django.urls import path

from . import views

urlpatterns = [
    path('create-url/', views.create_url, name='create-url'),
    path('delete-url/<int:pk>/', views.delete_url, name='delete-url')
]
