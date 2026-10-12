from django.db import models


class University(models.Model):
    name = models.CharField(max_length=255)
    location_name = models.CharField(
        max_length=255,
        help_text="General location e.g. Dar es Salaam, Tanzania",
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='universities/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name


class Campus(models.Model):
    university = models.ForeignKey(
        University,
        related_name='campuses',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=255,
        help_text="Campus name e.g. Main Campus, Mabibo Campus",
    )
    location_name = models.CharField(
            max_length=255,
            help_text="General location e.g. Dar es Salaam, Tanzania",
        )
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='campuses/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Campuses"

    def __str__(self):
        return f"{self.university.name} - {self.name}"