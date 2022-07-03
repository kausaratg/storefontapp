from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Post(models.Model):
    img = models.ImageField(upload_to='posts')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Register(models.Model):
    profile = models.ForeignKey(User, on_delete= models.CASCADE)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)

    def __str__(self):
        return self.f_name
class Message(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
