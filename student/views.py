from django.shortcuts import render


def group(request):
    return render(request, 'student/group.html', {})


def info(request):
    return render(request, 'student/info.html', {})


def reyting(request):  # noqa
    return render(request, 'student/reyting.html', {})


def students(request):
    return render(request, 'student/students.html', {})


def shop(request):
    return render(request, 'student/shop.html', {})
