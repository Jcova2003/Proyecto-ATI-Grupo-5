# main_app/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import login_view

urlpatterns = [
    path("", views.home, name="home"),
    path("notifications/", views.notifications, name="notifications"),
    path('chats/', views.chats_view, name='chats'),
    path("chat/", views.chat_with_friend, name="chat_with_friend"),
    path('login/', login_view, name='login'),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='my_profile'),
    path("profile/<int:id_usuario>", views.profile, name="profile"),
    path("post/<int:id_publicacion>", views.post, name="post"),
]
