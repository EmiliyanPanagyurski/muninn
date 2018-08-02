from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from api.models.game import Publisher
from api.views.serializers import PublisherSerializer
from .factories import PublisherFactory


class PublisherViewTestCase(APITestCase):
    def setUp(self):
        self.publisher = PublisherFactory(name='dev', website='dev.com')
        self.publisher.save()

    def test_request_all_publishers(self):
        url = reverse('publishers-all')
        response = self.client.get(url, format='json')
        publishers = Publisher.objects.all()
        serialize = PublisherSerializer(publishers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_filter_by_status(self):
        url = reverse('publishers-filtered')
        filter_url = url + '?status=unknown'
        response = self.client.get(filter_url, format='json')
        publishers = Publisher.objects.all()
        serialize = PublisherSerializer(publishers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_search_request(self):
        url = reverse('publishers-filtered')
        filter_url = url + '?search=dev'
        response = self.client.get(filter_url, format='json')
        publishers = Publisher.objects.all()
        serialize = PublisherSerializer(publishers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])

    def test_get_publisher_by_name(self):
        url = reverse('publisher-name', args=['dev'])
        response = self.client.get(url, format='json')
        publisher = Publisher.objects.all()
        serialize = PublisherSerializer(publisher[0])
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data)

