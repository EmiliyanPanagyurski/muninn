from rest_framework import viewsets
from ..models.engine import Engine
from .serializers import EngineSerializer


class EngineView(viewsets.ModelViewSet):
    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
