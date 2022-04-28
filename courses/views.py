from django.shortcuts import render
from courses.models import course, student, teacher

# Create your views here.
def courses_index(request):
    courses = course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses_index.html', context)

def courses_detail(request, pk):
    coursee = course.objects.get(pk=pk)
    context = {
        'course': coursee,
    }
    return render(request, 'course.detail.html', context)
    
def teacher_detail(request, pk):
    teachers = teacher.objects.get(pk=pk)
    context = {
        'teacher': teachers,
    }
    return render(request, 'teacher.detail.html', context)

def student_detail(request, pk):
    students = student.objects.get(pk=pk)
    context = {
        'student': students,
    }
    return render(request, 'student.detail.html', context)