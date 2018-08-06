from django.test import TestCase
from ..models.publisher import Publisher
from .MockData import TESTDATA


class PublisherTestCase(TestCase):
    def setUp(self):
        self.name = TESTDATA['name']
        self.website = TESTDATA['website']
        self.headquarters = TESTDATA['headquarters']
        self.founded = TESTDATA['founded']
        self.status = TESTDATA['status']
        self.revenue = TESTDATA['revenue']
        self.publisher = Publisher(name=self.name,
                                   website=self.website,
                                   headquarters=self.headquarters,
                                   founded=self.founded,
                                   status=self.status,
                                   revenue=self.revenue)

    def test_model_creates_Publisher(self):
        old_count = Publisher.objects.count()
        self.publisher.save()
        count = Publisher.objects.count()
        self.assertNotEqual(count, old_count)

    def test_publisher_name(self):
        self.assertEquals(self.name, self.publisher.name)

    def test_publisher_website(self):
        self.assertEquals(self.website, self.publisher.website)

    def test_publisher_headquarters(self):
        self.assertEquals(self.headquarters, self.publisher.headquarters)

    def test_publisher_founded(self):
        self.assertEquals(self.founded, self.publisher.founded)

    def test_publisher_status(self):
        self.assertEquals(self.status, self.publisher.status)

    def test_publisher_revenue(self):
        self.assertEquals(self.revenue, self.publisher.revenue)
