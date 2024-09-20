from django.urls import path
from .views import (
    index, reyting,
    group, student,
    info, user
)

app_name = 'mentor'

urlpatterns = [
    path("index/", index, name="index"),
    path("reyting/", reyting, name="reyting"),
    path("group/", group, name="group"),
    path("student/", student, name="student"),
    path("info/", info, name="info"),
    path("user/", user, name="user"),
]