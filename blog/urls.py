from django.urls import path
from . import views

urlpatterns=[
    path('posts',  views.IndexView.as_view(), name='index'),
    path('author/<int:author_pk>/',views.PostFilter.as_view(), name='post_by_author' ),
    path('posts/<int:pk>',  views.PostView.as_view(), name='post_detail'),
    
]