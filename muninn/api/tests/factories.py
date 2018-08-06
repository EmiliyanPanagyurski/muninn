import factory

from api.models.game import Game
from api.models.developer import Developer
from api.models.publisher import Publisher
from api.models.engine import Engine
from .MockData import TESTDATA


class DeveloperFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Developer

    name = TESTDATA['name']
    website = TESTDATA['website']
    headquarters = TESTDATA['headquarters']
    founded = TESTDATA['founded']
    status = TESTDATA['status']
    industry = TESTDATA['industry']
    founder = TESTDATA['founder']
    number_employees = TESTDATA['number_employees']
    products = TESTDATA['products']


class PublisherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Publisher

    name = TESTDATA['name']
    website = TESTDATA['website']
    headquarters = TESTDATA['headquarters']
    founded = TESTDATA['founded']
    status = TESTDATA['status']
    revenue = TESTDATA['revenue']


class EngineFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Engine

    name = TESTDATA['name']
    website = TESTDATA['website']
    developer = factory.SubFactory(DeveloperFactory)
    initial_release = TESTDATA['initial_release']
    stable_release = TESTDATA['stable_release']


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = TESTDATA['name']
    genre = TESTDATA['genre']
    description = TESTDATA['description']
    developer = factory.SubFactory(DeveloperFactory)
    publisher = factory.SubFactory(PublisherFactory)
    platforms = TESTDATA['platforms']
    engine = factory.SubFactory(EngineFactory)
    series = TESTDATA['series']
    release_date = TESTDATA['release_date']