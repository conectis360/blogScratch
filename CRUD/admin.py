from django.contrib import admin
from .models import BlogPost, BlogTag

# Register your models here.
admin.site.register(BlogPost)
admin.site.register(BlogTag)