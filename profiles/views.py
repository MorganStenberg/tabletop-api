from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.response import Response
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from table_tt_api.permissions import IsOwnerOrReadOnly

class ProfileList(APIView):
    """
    Profile list view - credit to Code Institute Walkthrough, link in readme
    """
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True, context={'request': request})
        return Response(serializer.data)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        review_count=Count('owner__review', distinct=True),
        
    ).order_by('-created_at')
    