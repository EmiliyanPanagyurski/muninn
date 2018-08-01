from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from ..models.game import Game
from .serializers import GameSerializer
from .pagination import CustomPagination


class GameView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'genre', 'series', 'publisher__name', 'engine__name', 'developer__name') # noqa
    search_fields = ('name', 'genre', 'series', 'publisher__name', 'engine__name', 'developer__name') # noqa
