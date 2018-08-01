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
        url = reverse('publishers')
        response = self.client.get(url, format='json')
        publishers = Publisher.objects.all()
        serialize = PublisherSerializer(publishers, many=True)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(serialize.data, response.data['results'])
