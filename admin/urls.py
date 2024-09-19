from django.urls import path
from .views import (
    index, reyting,
    mentor, student,
    info, user
)

urlpatterns = [
    path("index/", index, name="index"),
    path("reyting/", reyting, name="reyting"),
    path("mentor/", mentor, name="mentor"),
    path("student/", student, name="student"),
    path("info/", info, name="info"),
    path("user/", user, name="user"),
]