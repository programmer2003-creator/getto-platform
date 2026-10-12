from django.db import models

# Create your models here.

class Notification(models.Model):
    class RecipientType(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        OWNER = "owner", "Owner"
        STAFF = "staff", "Staff"

    class Channel(models.TextChoices):
        IN_SYSTEM = "in_system", "In System"
        EMAIL = "email", "Email"
        SMS = "sms", "SMS"

    recipient_type = models.CharField(
        max_length=20,
        choices=RecipientType.choices,
    )
    recipient_id = models.BigIntegerField()
    title = models.CharField(
        max_length=150,
    )
    message = models.TextField()
    channel = models.CharField(
        max_length=20,
        choices=Channel.choices,
        default=Channel.IN_SYSTEM,
    )
    is_read = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField()

    class Meta:
        db_table = "notifications"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
