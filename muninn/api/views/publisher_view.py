from rest_framework import viewsets
from ..models.publisher import Publisher
from .serializers import PublisherSerializer


class PublisherView(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
