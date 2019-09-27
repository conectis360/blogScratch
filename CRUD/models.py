from django.db import models
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    text_body = models.TextField()
    escritor = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title