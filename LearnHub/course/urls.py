from django.urls import path
from .views import *
urlpatterns = [
    path('courseHome/',course_home, name='courseHome'),
    path('course_add/',add_course,name="add_course"),
    
    path('course_update/<int:id>/',update_course,name="update_course"),
    path('course_delete/<int:id>/',delete_course,name="delete_course"),

]
