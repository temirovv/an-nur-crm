# Generated by Django 4.2.16 on 2024-09-20 04:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import student.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Ism va familiya faqat harflardan iborat bo‘lishi kerak, raqam yoki belgilar bo‘lmasligi kerak.', regex='^[a-zA-Z]+$')])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Ism va familiya faqat harflardan iborat bo‘lishi kerak, raqam yoki belgilar bo‘lmasligi kerak.', regex='^[a-zA-Z]+$')])),
                ('image', models.ImageField(upload_to='mentors/', validators=[student.validators.validate_image_format, student.validators.validate_image_size])),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Telefon raqami +998 bilan boshlanishi va 12 ta belgidan iborat bo‘lishi kerak.', regex='^\\+998\\d{9}$')])),
                ('birth_year', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('starting', 'Starting'), ('studying', 'Studying'), ('not_studying', 'Not Studying')], default='starting', max_length=20)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('silver', models.PositiveIntegerField(default=0)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizer.group')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
