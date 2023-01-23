from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('users/', views.UserList.as_view()),
    path('user/<str:pk>/', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('post/<str:pk>/', views.PostDetail.as_view()),
]
