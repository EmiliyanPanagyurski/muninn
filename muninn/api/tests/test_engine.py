from django.test import TestCase
from ..models.engine import Engine
from .factories import DeveloperFactory
from .MockData import TESTDATA


class EngineTestCase(TestCase):
    def setUp(self):
        self.name = TESTDATA['name']
        self.developer = DeveloperFactory()
        self.initial_release = TESTDATA['initial_release']
        self.stable_release = TESTDATA['stable_release']
        self.website = TESTDATA['website']
        self.engine = Engine(name=self.name,
                             developer=self.developer,
                             initial_release=self.initial_release,
                             stable_release=self.stable_release,
                             website=self.website)

    def test_model_creates_engine(self):
        old_count = Engine.objects.count()
        self.engine.save()
        count = Engine.objects.count()
        self.assertNotEqual(count, old_count)

    def test_engine_name(self):
        self.assertEquals(self.name, self.engine.name)

    def test_engine_initial_release(self):
        self.assertEquals(self.initial_release, self.engine.initial_release)

    def test_engine_stable_release(self):
        self.assertEquals(self.stable_release, self.engine.stable_release)

    def test_engine_website(self):
        self.assertEquals(self.website, self.engine.website)

    def test_engine_developer(self):
        self.assertEquals(self.developer, self.engine.developer)
