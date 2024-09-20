from django.urls import path
from .views import (
    index, reyting,
    mentor, student,
    info, user, grade,
    request, annu_index
)

app_name = "organizer"

urlpatterns = [
    path("index/", index, name="index"),
    path("reyting/", reyting, name="reyting"),
    path("mentor/", mentor, name="mentor"),
    path("student/", student, name="student"),
    path("info/", info, name="info"),
    path("user/", user, name="user"),
    path("grade/", grade, name="grade"),

    path("request/", request, name="request"),
    path("", annu_index, name="annu_index"),
]