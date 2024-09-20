from django.urls import path
from .views import group, info, reyting, shop, students


app_name = 'student'

urlpatterns = [
    path('group/', group, name='group'),
    path('info/', info, name='info'),
    path('reyting/', reyting, name='reyting'),
    path('shop/', shop, name='shop'),
    path('students/', students, name='students')
]
