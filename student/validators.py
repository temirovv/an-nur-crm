from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import os

 
name_validator = RegexValidator(
    regex=r'^[a-zA-Z]+$',
    message='Ism va familiya faqat harflardan iborat bo‘lishi kerak, raqam yoki belgilar bo‘lmasligi kerak.'
)

 
def validate_image_format(image):
    ext = os.path.splitext(image.name)[1].lower()
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if ext not in valid_extensions:
        raise ValidationError('Rasm faqat JPEG, JPG yoki PNG formatlarda bo‘lishi kerak.')

 
def validate_image_size(image):
    limit = 2 * 1024 * 1024   
    if image.size > limit:
        raise ValidationError('Rasm hajmi maksimal 2MB bo‘lishi kerak.')

phone_number_validator = RegexValidator(
    regex=r'^\+998\d{9}$',
    message='Telefon raqami +998 bilan boshlanishi va 12 ta belgidan iborat bo‘lishi kerak.'
)
