
from django.urls import path

from . import views

urlpatterns = [
    path('api/save_chat_message/', views.save_chat_message),
    path('api/message', views.MessageList.as_view()),
    path('api/message/<int:pk>/', views.MessageDetail.as_view()),
    path('api/user', views.CustomUserList.as_view()),
    path('api/user/<int:pk>/', views.CustomUserDetail.as_view())
]
