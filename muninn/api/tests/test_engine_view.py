from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models.game import Engine
from api.views.serializers import EngineSerializer
from .factories import EngineFactory


class EngineViewTestCase(APITestCase):
    def setUp(self):
        self.engine = EngineFactory(name='dev', website='dev.com')
        self.engine.save()

    def test_request_all_engines(self):
        url = reverse('engines')
        response = self.client.get(url, format='json')
        engines = Engine.objects.all()
        serialize = EngineSerializer(engines, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])
