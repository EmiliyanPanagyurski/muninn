from django.db import models
from .developer import Developer
from .publisher import Publisher
from .engine import Engine


class Game(models.Model):
    """ Model representing a game """
    name = models.CharField(max_length=30)
    genre = models.TextField()
    description = models.TextField()
    developer = models.ForeignKey(Developer,
                                  on_delete=models.SET_NULL,
                                  null=True)
    publisher = models.ForeignKey(Publisher,
                                  on_delete=models.SET_NULL,
                                  null=True)
    platforms = models.CharField(max_length=50)
    engine = models.ForeignKey(Engine,
                               on_delete=models.SET_NULL,
                               null=True)
    series = models.CharField(max_length=50)
    release_date = models.DateField()

    class Meta:
        db_table = 'Games'
        unique_together = ('name', 'series')

    def __str__(self):
        return self.name
