from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'common/home.html')

def aboutus(request):
    return render(request, 'common/about us.html')

def contact(request):
    return render(request, 'common/contact us.html')

def admission(request):
    return render(request, 'common/admission.html')

def master(request):
    return render(request, 'common/master.html')














