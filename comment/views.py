from rest_framework import generics, permissions
from tech_roadmap_root.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# Create your views here.
"""
Using generic will save much time because it 
comes with most of the method user need to 
GET, POST, UPDATE and DELETE
You need just to learn the syntax
"""

class CommentList(generics.ListCreateAPIView):
    """
    List all the available comments 
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
