from rest_framework import viewsets
from ..models.developer import Developer
from .serializers import DeveloperSerializer


class DeveloperView(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
