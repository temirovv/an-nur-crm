from django.db import models
from organizer.models import Group
from .validators import  (
    name_validator, validate_image_format, 
    validate_image_size, phone_number_validator 
)
from shared.models import BaseModel
 

class Student(BaseModel):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    STATUS_CHOICES = [
        ('starting', 'Starting'),
        ('studying', 'Studying'),
        ('not_studying', 'Not Studying'),
    ]

    first_name = models.CharField(
        max_length=50,
        validators=[name_validator]   
    )
    last_name = models.CharField(
        max_length=50,
        validators=[name_validator]   
    )
    image = models.ImageField(
        upload_to='mentors/',
        validators=[validate_image_format, validate_image_size]  
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[phone_number_validator]  
    )    
    birth_year = models.PositiveIntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)   
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='starting')  # Holat
    username = models.CharField(max_length=150, unique=True)  # Foydalanuvchi nomi
    password = models.CharField(max_length=128)  # Parol
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    silver = models.PositiveIntegerField(default=0)  # Silver maydoni, dastlabki qiymati 0

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
