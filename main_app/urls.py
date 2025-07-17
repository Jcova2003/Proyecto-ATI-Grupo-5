# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("feed/", views.feed, name="feed"),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),
    path("notifications/", views.notifications, name="notifications"),
    path('chat/<str:friend_name>/', views.chat_with_friend, name='chat_with_friend'),
]
