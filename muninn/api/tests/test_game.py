from django.test import TestCase
from ..models.game import Game
from .MockData import TESTDATA
from .factories import DeveloperFactory, PublisherFactory, EngineFactory


class GameTestCase(TestCase):
    def setUp(self):
        self.name = TESTDATA['name']
        self.genre = TESTDATA['genre']
        self.description = TESTDATA['description']
        self.developer = DeveloperFactory()
        self.publisher = PublisherFactory()
        self.engine = EngineFactory(developer=self.developer)
        self.platforms = TESTDATA['platforms']
        self.series = TESTDATA['series']
        self.release_date = TESTDATA['release_date']
        self.game = Game(name=self.name,
                         genre=self.genre,
                         description=self.description,
                         developer=self.developer,
                         publisher=self.publisher,
                         engine=self.engine,
                         platforms=self.platforms,
                         series=self.series,
                         release_date=self.release_date)

    def test_model_create_game(self):
        old_count = Game.objects.count()
        self.game.save()
        count = Game.objects.count()
        self.assertNotEqual(count, old_count)

    def test_game_name(self):
        self.assertEquals(self.name, self.game.name)

    def test_game_genre(self):
        self.assertEquals(self.genre, self.game.genre)

    def test_game_description(self):
        self.assertEquals(self.description, self.game.description)

    def test_game_developer(self):
        self.assertEquals(self.developer, self.game.developer)

    def test_game_publisher(self):
        self.assertEquals(self.publisher, self.game.publisher)

    def test_game_engine(self):
        self.assertEquals(self.engine, self.game.engine)

    def test_game_series(self):
        self.assertEquals(self.series, self.game.series)

    def test_game_platforms(self):
        self.assertEquals(self.platforms, self.game.platforms)

    def test_game_release_date(self):
        self.assertEquals(self.release_date, self.game.release_date)
