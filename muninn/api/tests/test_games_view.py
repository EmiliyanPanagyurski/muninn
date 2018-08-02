from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models.game import Game
from api.views.serializers import GameSerializer
from .factories import GameFactory, DeveloperFactory


class GamesViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('games')
        self.developer = DeveloperFactory(name='dev', website='dev.com')
        self.game = GameFactory(developer=self.developer)
        self.game.save()

    def test_request_all_games(self):
        response = self.client.get(self.url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_request(self):
        filter_url = self.url + '?name=test'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_search_request(self):
        filter_url = self.url + '?search=test'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])
