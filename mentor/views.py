from django.shortcuts import render

 
def index(request):
    return render(request, 'mentor/index.html', {})


def group(request):
    return render(request, 'mentor/group.html', {})


def info(request):
    return render(request, 'mentor/info.html', {})


def reyting(request):
    return render(request, 'mentor/reyting.html', {})


def student(request):
    return render(request, 'mentor/student.html', {})


def user(request):
    return render(request, 'mentor/user.html', {})