from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=30)
    study_year= models.IntegerField()
    enrollment_date = models.DateField()
    image = models.ImageField(upload_to='students_images/', blank=True, null=True)  # ← الصورة

    #ينفع تتحط في الCourse 
    # بس هتبقى كده 
    ### students = models.ManyToManyField(Student)  # ← العلاقة m:n
    
    ## Student على طول لو عامل import فوق
    ##لو لا بتعمل ال  'course.Course' // 'student.Student'

    courses = models.ManyToManyField('course.Course')  # ←  العلاقة m:n

    

    def __str__(self):
        return f"{self.name}"
    
    def get_courses(self):
        return ", ".join([course.name for course in self.courses.all()])
    get_courses.short_description = 'Courses'
    get_courses.admin_order_field = 'courses'
    # عشان اعرض الكورسات في ال admin panel
    # وكمان عشان اقدر افرز بيها
    #  admin_order_field  دي بتخلي العمود ده يتفرز في ال admin panel
    