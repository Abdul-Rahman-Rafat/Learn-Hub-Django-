
from django.urls import path
from . import views
from django.shortcuts import redirect
from student import views as st
from course import views as co


urlpatterns = [
    path('register/', views.register_view if hasattr(views, 'register_view') else views.register_page, name='register'),
    path('login/', views.login_view if hasattr(views, 'login_view') else views.login_page, name='login'),
    path('logout/', views.logout_view if hasattr(views, 'logout_view') else (lambda r: redirect('home')), name='logout'),
    
]
