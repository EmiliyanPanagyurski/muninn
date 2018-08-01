from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter

from ..models.publisher import Publisher
from .serializers import PublisherSerializer
from .pagination import CustomPagination


class PublisherView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('name', 'status')
    search_fields = ('name', 'status')
