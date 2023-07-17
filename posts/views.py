from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PostListView(generics.ListCreateAPIView):
    serializer_class=PostSerializer
    queryset = Post.objects.all()
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



