
from django.urls import path

from . import views

urlpatterns = [
    path('api/save_chat_message/', views.save_chat_message),
    path('api/', views.MessageList.as_view()),
    path('snippets/<int:pk>/', views.MessageDetail.as_view())
]
