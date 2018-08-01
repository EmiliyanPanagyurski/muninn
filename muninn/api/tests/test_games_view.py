from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models.game import Game
from api.views.serializers import GameSerializer
from .factories import GameFactory, DeveloperFactory


class GamesViewTestCase(APITestCase):
    def setUp(self):
        self.developer = DeveloperFactory(name='dev', website='dev.com')
        self.game = GameFactory(developer=self.developer)
        self.game.save()

    def test_request_all_games(self):
        url = reverse('games')
        response = self.client.get(url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])
