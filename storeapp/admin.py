from django.contrib import admin
from .models import Post, Register,  Message

# Register your models here.
admin.site.register(Post)
admin.site.register(Register)
admin.site.register(Message)
