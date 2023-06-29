
from django.urls import path

from . import views

urlpatterns = [
    path('api/save_chat_message/', views.save_chat_message),
    path('api/', views.MessageList.as_view()),
    path('snippets/<int:pk>/', views.MessageDetail.as_view()),
    path('api/chat', views.ChatMessageList.as_view()),
    path('api/chat/<str:pk>/', views.ChatMessageDetail.as_view()),
    path('api/users', views.CustomUserList.as_view()),
    path('api/users/login', views.login_view),
    path('api/users/<str:pk>/', views.CustomUserDetail.as_view()),
]
