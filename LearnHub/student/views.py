from django.shortcuts import render ,redirect
from .models import Student
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def student_home(request):
    data = Student.objects.all()
    return render(request, 'student/home.html',{'students_jinja': data})





def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('studHome')
    else:
        form = StudentForm()
    return render(request, 'student/add_student.html', {'form': form})




def view_student(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'student/view_student.html', {'student': student})

def update_student(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('studHome')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/update_student.html', {'form': form})
    # return render(request, 'student/add_student.html', {'form': form}) # you can also reuse the add_student.html template

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('studHome')

