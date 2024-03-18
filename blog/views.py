from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, CreateView,DetailView
from . import models



# Create your views here.
class IndexView(ListView):
    template_name = "blog/post_list.html"
    model = models.Post
    context_object_name = "posts"
    
class PostView(DetailView):
    template_name = "blog/post_detail.html"
    model = models.Post
    context_object_name = "post"
    

        
        
    
# render(request,'html',context)


class PostFilter(IndexView):
    
    def get_queryset(self) :
        author_pk = self.kwargs.get('author_pk')
        author = models.Author.objects.get(id=author_pk)
        queryset = super().get_queryset()
        queryset = queryset.filter(author=author)
        return queryset
        
    

