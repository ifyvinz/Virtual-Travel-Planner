from django.contrib import admin
from .models import User, Post, Trip, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Trip)
admin.site.register(Comment)
#admin.site.register(Rating)
