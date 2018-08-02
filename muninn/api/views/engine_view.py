from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from ..models.engine import Engine
from .serializers import EngineSerializer
from .pagination import CustomPagination
from .filter import CaseInsensitiveFilter


class EngineListAllView(ListAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    pagination_class = CustomPagination


class EngineListAllFilteredView(EngineListAllView):
    filter_backends = (SearchFilter, CaseInsensitiveFilter)
    filter_fields = ('developer',)
    search_fields = ('name', 'developer__name')


class EngineRetrieveView(RetrieveAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    lookup_field = 'name'
    lookup_url_kwarg = 'name'
