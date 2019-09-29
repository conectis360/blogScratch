from django.db import models
from django.urls import reverse

class BlogTag(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=48)
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    
class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    text_body = models.TextField()
    tags = models.ManyToManyField(BlogTag, blank=True)
    escritor = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title
    
