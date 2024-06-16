# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(_('First Name'), max_length=100)
    last_name = models.CharField(_('Last Name'), max_length=100)
    email = models.EmailField(_('Email Address'), max_length=254, unique=True)
    username = models.CharField(_('Username'), max_length=100, unique=True, default='default_username')
    gender = models.CharField(_('Gender'), max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male')
    userphoto = models.ImageField(_('User Photo'), upload_to='userphotos/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username', 'gender']

    objects = CustomUserManager()

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
class Test(models.Model):
    
    MY_CHOICES = [
        ('Katta sinflar', 'Katta sinflar'),
        ('Kichik sinflar', 'Kichik sinflar'),
    ]
    subjects=[
        ('Dasturlash', 'Dasturlash'),
        ('Matematika', 'Matematika'),
        ('Fizika','Fizika')
    ]
    question_str=models.TextField(blank=True) 
    question_img=models.ImageField(blank=True)
    question_type1=models.CharField(max_length=100,choices=MY_CHOICES)
    question_subject=models.CharField(max_length=15,choices=subjects)
    option1=models.TextField()
    option2=models.TextField()
    option3=models.TextField()
    option4=models.TextField()
    def __str__(self) -> str:
        return f"{self.question_str} {self.question_img}"
class Result(models.Model):
    check_student=models.IntegerField()
    user_id=models.OneToOneField(User,on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f"{self.check_student}" 

class Lesson2(models.Model):
    title = models.CharField(max_length=200)
    photo = models.URLField()
    information = models.TextField()

    def __str__(self) -> str:
        return self.title






