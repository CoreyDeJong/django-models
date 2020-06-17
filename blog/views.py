from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.

class HomeView(ListView):
    template_name = 'home.html'
    model = Post

# class PostPageView(TemplateView):
#     template_name = 'base.html'
    
class PostDetailsView(DetailView):
    template_name = 'post_detail.html'
    model = Post
