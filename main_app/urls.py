# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("notifications/", views.notifications, name="notifications"),
    path('chat/', views.chat_with_friend, name='chat_with_friend'),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='my_profile'),
    path("profile/<int:id_usuario>", views.profile, name="profile"),
]
