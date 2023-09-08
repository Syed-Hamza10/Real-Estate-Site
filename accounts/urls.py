"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', views.login_view, name= 'login'),
    path('register/', views.register, name= 'register'),
    path('logout/', views.logout_view, name= 'logout'),
    path('delete/', views.delete_view, name= 'delete'),
    path('users_list/', views.users_list, name='users_list'),
    path('send_request/<int:receiver_id>/', views.send_friend_request, name='send_friend_request'),
    
    path('accept_request/<int:request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('decline_request/<int:request_id>/', views.decline_friend_request, name='decline_friend_request'),
    path('friend-requests/', views.friend_request_list_view, name='friend_request_list'),
    path('accepted-friends/', views.accepted_friends_list_view, name='accepted_friends_list'),
    path('send/<int:recipient_id>/', views.send_message, name='send_message'),
    path('chat/<int:recipient_id>/', views.chat_with, name='chat_with'),
    
]

