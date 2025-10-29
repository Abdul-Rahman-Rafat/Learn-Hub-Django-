from django.urls import path
from .views import *

urlpatterns = [
    path('studentHome/',student_home, name='studHome'),
    path('student_add/',add_student,name="add_student"),

        path('student_view/<int:id>/',view_student,name="view_student"),

    path('update/<int:id>/', update_student, name='update_student'),
    path('delete/<int:id>/', delete_student, name='delete_student'),
]
