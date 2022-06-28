from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()
class Post(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(models.Model):
    User = models.ForeignKey(User, on_delete= models.CASCADE)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        return self.f_name

class Message(models.Model):
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email
