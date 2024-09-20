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

def grade(request):
    return render(request, 'admin/grade/grade.html', {})



def annu_index(request):
    return render(request, 'annur-site/index.html', {})


def request(request):
    return render(request, 'annur-site/request.html', {})