from django.shortcuts import render
from rest_framework import generics,permissions
from .permessions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from .models import Post

class PostListView(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) #это уже не понадобиться потому что я уже изменил это в settings.py
    serializer_class=PostSerializer
    queryset = Post.objects.all()

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer



