from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    text_body = models.TextField()
    escritor = models.ForeignKey(
        'auth.User', 
        on_delete=models.CASCADE
    )