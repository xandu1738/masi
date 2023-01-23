from rest_framework import mixins, generics
from django.contrib.auth.models import User
from .models import Post
from .serializers import UserSerializer, PostSerializer
from django.http import JsonResponse

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def perform_create(self, serializer):
        return serializer.create(owner=self.request.user)
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def welcome(request):
    return JsonResponse({'message': 'welcome'})