from django.db import models
from .entities import Entities


class Publisher(Entities):
    """ Model representing a pubisher """
    revenue = models.CharField(max_length=30)

    class Meta:
        db_table = 'Publishers'
        unique_together = ('name', 'website')

    def __str__(self):
        return self.name
