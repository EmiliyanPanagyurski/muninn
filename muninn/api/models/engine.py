from django.db import models
from .developer import Developer


class Engine(models.Model):
    name = models.CharField(max_length=30)
    developer = models.ForeignKey(Developer,
                                  on_delete=models.SET_NULL,
                                  null=True)
    initial_release = models.CharField(max_length=30)
    stable_release = models.CharField(max_length=30)
    website = models.URLField()

    class Meta:
        db_table = 'Engines'
        unique_together = ('name', 'website')

    def __str__(self):
        return self.name
