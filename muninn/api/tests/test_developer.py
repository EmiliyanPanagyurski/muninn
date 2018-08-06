from django.test import TestCase
from ..models.developer import Developer
from .MockData import TESTDATA


class DeveloperTestCase(TestCase):
    def setUp(self):
        self.name = TESTDATA['name']
        self.website = TESTDATA['website']
        self.headquarters = TESTDATA['headquarters']
        self.founded = TESTDATA['founded']
        self.status = TESTDATA['status']
        self.industry = TESTDATA['industry']
        self.founder = TESTDATA['founder']
        self.number_employees = TESTDATA['number_employees']
        self.products = TESTDATA['products']
        self.developer = Developer(name=self.name,
                                   website=self.website,
                                   headquarters=self.headquarters,
                                   founded=self.founded,
                                   status=self.status,
                                   industry=self.industry,
                                   founder=self.founder,
                                   number_employees=self.number_employees,
                                   products=self.products)

    def test_model_can_create_developer(self):
        old_count = Developer.objects.count()
        self.developer.save()
        count = Developer.objects.count()
        self.assertNotEqual(old_count, count)

    def test_developer_name(self):
        self.assertEquals(self.name, self.developer.name)

    def test_developer_website(self):
        self.assertEquals(self.website, self.developer.website)

    def test_developer_headquarters(self):
        self.assertEquals(self.headquarters, self.developer.headquarters)

    def test_developer_founded(self):
        self.assertEquals(self.founded, self.developer.founded)

    def test_developer_status(self):
        self.assertEquals(self.status, self.developer.status)

    def test_developer_industry(self):
        self.assertEquals(self.industry, self.developer.industry)

    def test_developer_founder(self):
        self.assertEquals(self.founder, self.developer.founder)

    def test_developer_number_employees(self):
        self.assertEquals(self.number_employees,
                          self.developer.number_employees)

    def test_developer_products(self):
        self.assertEquals(self.products, self.developer.products)
