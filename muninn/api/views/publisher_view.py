from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from ..models.publisher import Publisher
from .serializers import PublisherSerializer
from .pagination import CustomPagination
from .filter import CaseInsensitiveFilter


class PublisherListView(ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    pagination_class = CustomPagination


class PublisherListAllFilteredView(PublisherListView):
    filter_backends = (SearchFilter, CaseInsensitiveFilter)
    filter_fields = ('status',)
    search_fields = ('name', 'status')


class PublisherRetrieveView(RetrieveAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
    lookup_field = 'name'
    lookup_url_kwarg = "name"
