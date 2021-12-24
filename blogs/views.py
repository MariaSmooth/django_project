from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView , DetailView , TemplateView
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.urls import reverse_lazy
from .models import Post
 
 
class BlogListView(ListView):
    model = Post
    template_name = 'blogs/home.html'
    context_object_name = 'all_posts_list'

class BlogDetailView(DetailView): 
    model = Post
    template_name = 'blogs/details.html'

class BlogCreateView(CreateView): 
    model = Post
    template_name = 'blogs/news.html'
    fields = ['title', 'author', 'text', "image"]

class BlogUpdateView(UpdateView): 
    model = Post
    template_name = 'blogs/edit.html'
    fields = ['title', 'text', "image"]

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blogs/delete.html'
    success_url = reverse_lazy('home')

class ShowListView(ListView):
    model = Post
    template_name = 'blogs/show.html'
    context_object_name = 'posts_list'
