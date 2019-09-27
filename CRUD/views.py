from django.shortcuts import render
from django.views.generic import DetailView
from .models import BlogPost

# Create your views here.

class BlogView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    