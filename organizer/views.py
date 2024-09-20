from django.shortcuts import render

 
def index(request):
    return render(request, 'admin/index.html', {})


def mentor(request):
    return render(request, 'admin/mentor.html', {})


def info(request):
    return render(request, 'admin/info.html', {})


def reyting(request):
    return render(request, 'admin/reyting.html', {})


def student(request):
    return render(request, 'admin/students.html', {})


def user(request):
    return render(request, 'admin/user.html', {})