from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from ..models.game import Game
from .serializers import GameSerializer
from .pagination import CustomPagination
from .filter import CaseInsensitiveFilter


class GameListAllView(ListAPIView):
    """ View returning all games """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = CustomPagination


class GameListAllFilteredView(GameListAllView):
    """ View returning filtered or queried games """
    filter_backends = (SearchFilter, CaseInsensitiveFilter)
    filter_fields = ('genre', 'series', 'publisher', 'engine', 'developer', 'platforms')
    search_fields = ('name', 'genre', 'series', 'publisher__name', 'engine__name', 'developer__name', 'platforms')


class GameRetrieveView(RetrieveAPIView):
    """ View returning a specific game """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
