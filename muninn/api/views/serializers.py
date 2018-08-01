from rest_framework.serializers import ModelSerializer
from ..models.developer import Developer
from ..models.publisher import Publisher
from ..models.engine import Engine
from ..models.game import Game


class DeveloperSerializer(ModelSerializer):
    class Meta:
        model = Developer
        fields = [
            'name',
            'website',
            'headquarters',
            'status',
            'founded',
            'industry',
            'founder',
            'products',
            'number_employees'
        ]


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = [
            'name',
            'website',
            'headquarters',
            'status',
            'founded',
            'revenue'
        ]


class EngineSerializer(ModelSerializer):
    class Meta:
        model = Engine
        fields = [
            'name',
            'developer',
            'initial_release',
            'stable_release',
            'website'
        ]
        depth = 2


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = [
            'name',
            'genre',
            'description',
            'developer',
            'publisher',
            'platforms',
            'engine',
            'series',
            'release_date'
        ]
        depth = 3
