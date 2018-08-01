from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from ..models.engine import Engine
from .serializers import EngineSerializer
from .pagination import CustomPagination


class EngineView(ListAPIView):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'developer__name')
    search_fields = ('name', 'developer__name')
