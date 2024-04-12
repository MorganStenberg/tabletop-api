from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from table_tt_api.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Game
from .serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """
    List a game or create a game
    """
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()

    filter_backends = [
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Gets a game, update, destroy
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = GameSerializer
    queryset = Game.objects.all()

class GenreChoices(APIView):
    """
    View to return list of genre choices for games
    """

    permissions_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        return Response(Game.genre_choices)