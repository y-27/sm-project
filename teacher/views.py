from django.shortcuts import render

# Create your views here.


def teacherlogin(request):
    return render(request, 'teacher/teacherlogin.html')
