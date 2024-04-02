from rest_framework import generics, permissions
from .models import Like
from .serializers import LikeSerializer
from table_tt_api.permissions import IsOwnerOrReadOnly


class LikeList(generics.ListCreateAPIView):
    """
    Creates and lists likes
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    Gets a like and deletes it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
