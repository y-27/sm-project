from django.shortcuts import render

# Create your views here.

def studentlogin(request):
    return render(request, 'student/studentlogin.html')

def studentview(request):
    return render(request, 'student/studentview.html')

def masterstu(request):
    return render(request, 'student/masterstu.html')


