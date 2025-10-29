from django.shortcuts import render,redirect
from .models import Course
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def course_home(request):
    data = Course.objects.all()
    return render(request, 'course/home.html',{'courses_jinja': data})



def add_course(request):
    from .forms import CourseForm
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseHome')
    else:
        form = CourseForm()
    return render(request, 'course/add_course.html', {'form': form})

def update_course(request, id):
    from .forms import CourseForm
    course = Course.objects.get(id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('courseHome')
    else:
        form = CourseForm(instance=course)
    #return render(request, 'course/add_course.html', {'form': form})
    return render(request, 'course/update_course.html', {'form': form})




def delete_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    return redirect('courseHome')
