from django.utils import timezone
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import BlogPost

# Create your views here.

class BlogView(DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super(BlogView , self).get_context_data(**kwargs)
        context['posts'] = BlogPost.objects.all()
        return context

    
class HomePageView(ListView):
    model = BlogPost
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
    