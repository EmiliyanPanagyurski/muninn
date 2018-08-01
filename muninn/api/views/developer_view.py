from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from ..models.developer import Developer
from .serializers import DeveloperSerializer
from .pagination import CustomPagination


class DeveloperListView(ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'status', 'industry')
    search_fields = ('name', 'status', 'industry')
