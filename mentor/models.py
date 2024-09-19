from django.db import models
from shared.models import BaseModel
from .validators import  (
    name_validator, validate_image_format, 
    validate_image_size, phone_number_validator 
)


class Mentor(BaseModel):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    TEACHING_AREA_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('graphic_design', 'Graphic Design'),
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
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birth_year = models.PositiveIntegerField()
    teaching_area = models.CharField(max_length=15, choices=TEACHING_AREA_CHOICES)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
