from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter

from ..models.developer import Developer
from .serializers import DeveloperSerializer
from .pagination import CustomPagination
from .filter import CaseInsensitiveFilter


class DeveloperListAllView(ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    pagination_class = CustomPagination


class DeveloperListAllFilteredView(DeveloperListAllView):
    filter_backends = (SearchFilter, CaseInsensitiveFilter)
    filter_fields = ('status', 'industry')
    search_fields = ('name',)


class DeveloperRetrieveView(RetrieveAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    lookup_field = 'name'
    lookup_url_kwarg = "name"
