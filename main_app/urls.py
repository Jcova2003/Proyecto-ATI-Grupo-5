# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notifications/", views.notifications, name="notifications"),
    path('chat/', views.chat_with_friend, name='chat_with_friend'),
]
