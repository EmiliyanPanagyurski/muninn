from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from ..models.engine import Engine
from .serializers import EngineSerializer
from .pagination import CustomPagination
from .filter import CaseInsensitiveFilter


class EngineListAllView(ListAPIView):
    """ View for returning all game engines """
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    pagination_class = CustomPagination


class EngineListAllFilteredView(EngineListAllView):
    """ View for returning filtered or queried game engines """
    filter_backends = (SearchFilter, CaseInsensitiveFilter)
    filter_fields = ('developer',)
    search_fields = ('name', 'developer__name')


class EngineRetrieveView(RetrieveAPIView):
    """ View for returning a specific game engine """
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
