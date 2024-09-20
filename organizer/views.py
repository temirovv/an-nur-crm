from django.shortcuts import render
from .models import Group
 
def index(request):
    return render(request, 'admin/index.html', {})


def mentor(request):
    return render(request, 'organizer/mentor.html', {})


def info(request):
    return render(request, 'organizer/info.html', {})


def reyting(request):
    return render(request, 'organizer/reyting.html', {})


def student(request):
    return render(request, 'organizer/students.html', {})


def user(request):
    return render(request, 'organizer/user.html', {})

def grade(request):
    return render(request, 'adorganizermin/grade/grade.html', {})



def annu_index(request):
    return render(request, 'annur-site/index.html', {})


def request(request):
    return render(request, 'annur-site/request.html', {})