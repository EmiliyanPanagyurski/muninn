from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models.game import Developer
from api.views.serializers import DeveloperSerializer
from .factories import DeveloperFactory


class DeveloperViewTestCase(APITestCase):
    def setUp(self):
        self.developer = DeveloperFactory(name='dev', website='dev.com')
        self.developer.save()

    def test_request_all_developers(self):
        url = reverse('developers')
        response = self.client.get(url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])
