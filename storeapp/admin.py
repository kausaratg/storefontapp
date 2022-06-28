from django.contrib import admin
from .models import Post, User, Message

# Register your models here.
admin.site.register(Post)
admin.site.register(User)
admin.site.register(Message)
