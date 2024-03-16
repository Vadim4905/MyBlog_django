from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView
from . import models



# Create your views here.
class IndexView(ListView):
    template_name = "blog/post_list.html"
    model = models.Post
    context_object_name = "posts"
