from django.core.exceptions import ValidationError
from django.utils import timezone

def validate_start_time(start_time):
    if start_time < timezone.datetime.strptime("10:00", "%H:%M").time() or start_time > timezone.datetime.strptime("19:00", "%H:%M").time():
        raise ValidationError("Boshlanish vaqti 10:00 dan 19:00 gacha bo'lishi kerak.")

def validate_end_time(end_time, start_time):
    if end_time < timezone.datetime.strptime("12:00", "%H:%M").time() or end_time > timezone.datetime.strptime("21:00", "%H:%M").time():
        raise ValidationError("Tugash vaqti 12:00 dan 21:00 gacha bo'lishi kerak.")
    
    if end_time <= start_time:
        raise ValidationError("Tugash vaqti boshlanish vaqtidan keyin bo'lishi kerak.")
