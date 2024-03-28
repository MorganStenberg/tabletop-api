from .models import Save
from .serializers import SaveSerializer
from rest_framework import generics, permissions
from table_tt_api.permissions import IsOwnerOrReadOnly



class SaveList(generics.ListCreateAPIView):
    """
    List and create save instances
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SaveDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a save instance and delete it
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SaveSerializer
    queryset = Save.objects.all()
