from rest_framework.views import APIView
from django.db.models import Count
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from table_tt_api.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    """
    Lists reviews or create a review if user is logged in
    """
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Review.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it the user is the owner.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Review.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True),
    ).order_by('-created_at')