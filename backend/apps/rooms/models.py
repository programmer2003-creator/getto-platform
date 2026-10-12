
from django.contrib.gis.db import models
from apps.properties.models import Property

class Room(models.Model):
    property = models.ForeignKey(
        Property, 
        on_delete=models.CASCADE, 
        related_name='rooms',
        null=True, 
        blank=True
    )
    # Add optional fields present in your rooms table (e.g., price, room_type)
    
    class Meta:
        db_table = 'rooms'  # Maps directly to public.rooms in PostgreSQL

    def __str__(self):
        return f"Room {self.id}"