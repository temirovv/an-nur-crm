from django.db import models
from shared.models import BaseModel
from mentor.models import Mentor
from .validators import validate_start_time, validate_end_time   

class Group(BaseModel):
    GROUP_AREA_CHOICES = [
        ('backend', 'Backend'),
        ('frontend', 'Frontend'),
        ('graphic_design', 'Graphic Design'),
    ]
    name = models.CharField(max_length=100)  
    type = models.CharField(max_length=15, choices=GROUP_AREA_CHOICES)

    def __str__(self):
        return self.name
    


class MentorGroups(BaseModel):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)   
    group = models.ForeignKey(Group, on_delete=models.CASCADE) 
    start_time = models.TimeField(validators=[validate_start_time])   
    end_time = models.TimeField()  

    def clean(self):
        validate_end_time(self.end_time, self.start_time)   

    def __str__(self):
        return f"{self.name} ({self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')})"
  

    def __str__(self):
        return f"{self.mentor} - {self.group}"

