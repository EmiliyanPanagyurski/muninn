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
        url = reverse('developers-all')
        response = self.client.get(url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_industry(self):
        url = reverse('developers-filtered')
        filter_url = url + '?industry=test'
        response = self.client.get(filter_url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_status(self):
        url = reverse('developers-filtered')
        filter_url = url + '?status=unknown'
        response = self.client.get(filter_url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_search_request(self):
        url = reverse('developers-filtered')
        filter_url = url + '?search=dev'
        response = self.client.get(filter_url, format='json')
        developers = Developer.objects.all()
        serialize = DeveloperSerializer(developers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_get_developer_by_name(self):
        url = reverse('developer-name', args=['dev'])
        response = self.client.get(url, format='json')
        developer = Developer.objects.all()
        serialize = DeveloperSerializer(developer[0])
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data)
