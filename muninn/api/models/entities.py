from django.db import models


class Entities(models.Model):
    ACTIVE = 'active'
    DEFUNCT = 'defunct'
    UNKNOWN = 'unknown'
    STATUS_CHOICES = (
        (ACTIVE, 'Active'),
        (DEFUNCT, 'Defunct'),
        (UNKNOWN, 'Unknown')
    )
    name = models.CharField(max_length=30)
    website = models.URLField()
    headquarters = models.CharField(max_length=30)
    founded = models.CharField(max_length=30)
    status = models.CharField(max_length=7,
                              choices=STATUS_CHOICES,
                              default=UNKNOWN)

    class Meta:
        abstract = True
