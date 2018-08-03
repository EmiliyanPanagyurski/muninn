from django.db import models
from .entities import Entities


class Developer(Entities):
    """ Model that represents a developer """
    industry = models.CharField(max_length=30)
    number_employees = models.IntegerField()
    founder = models.CharField(max_length=30)
    products = models.CharField(max_length=30)

    class Meta:
        db_table = 'Developers'
        unique_together = ('name', 'website')

    def __str__(self):
        return self.name
