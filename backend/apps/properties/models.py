from django.contrib.gis.db import models

class Property(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    location = models.PointField(srid=4326, null=True, blank=True)

    class Meta:
        db_table = 'properties'

    def __str__(self):
        return self.title
    
