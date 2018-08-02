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
        url = reverse('games-all')
        response = self.client.get(url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_genre(self):
        url = reverse('games-filtered')
        filter_url = url + '?genre=test genre'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_series(self):
        url = reverse('games-filtered')
        filter_url = url + '?series=test series'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_platforms(self):
        url = reverse('games-filtered')
        filter_url = url + '?platfomrs=test, test, test'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_publisher_name(self):
        url = reverse('games-filtered')
        filter_url = url + '?publisher=test'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_developer_name(self):
        url = reverse('games-filtered')
        filter_url = url + '?developer=dev'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])
    
    def test_filter_by_engine_name(self):
        url = reverse('games-filtered')
        filter_url = url + '?engine=test'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_search_request(self):
        url = reverse('games-filtered')
        filter_url = url + '?search=test'
        response = self.client.get(filter_url, format='json')
        games = Game.objects.all()
        serialize = GameSerializer(games, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_get_game_by_name(self):
        url = reverse('game-name', args=['test'])
        response = self.client.get(url, format='json')
        game = Game.objects.all()
        serialize = GameSerializer(game[0])
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data)
