from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models.game import Developer
from api.views.serializers import DeveloperSerializer
from .factories import DeveloperFactory


class DeveloperViewTestCase(APITestCase):
    def setUp(self):
        self.url = reverse('developers')
        self.developer = DeveloperFactory(name='dev', website='dev.com')
        self.developer.save()

    def test_request_all_developers(self):
        response = self.client.get(self.url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_request(self):
        filter_url = self.url + '?name=dev'
        response = self.client.get(filter_url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_search_request(self):
        filter_url = self.url + '?search=dev'
        response = self.client.get(filter_url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])