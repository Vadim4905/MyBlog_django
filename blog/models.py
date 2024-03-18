from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('Author',on_delete=models.CASCADE,related_name='posts')
    
    def __str__(self):
        return self.title
    
    def published_recently(self):
        return timezone.now() - timedelta(days=7) < self.published_date
    
class Author(models.Model):
    name = models.CharField(max_length=63)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    auhtor_name = models.CharField(max_length=63)
    content = models.TextField()
    post = models.ForeignKey('Post',related_name='comments',on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.content

    
    
