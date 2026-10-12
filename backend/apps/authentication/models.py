from django.db import models

# Create your models here.

class PasswordReset(models.Model):
    class UserType(models.TextChoices):
        CUSTOMER = "customer", "Customer"
        OWNER = "owner", "Accommodation Owner"
        STAFF = "staff", "Staff"

    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
    )
    user_id = models.BigIntegerField()
    token = models.CharField(
        max_length=100,
        unique=True,
    )
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "password_resets"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.user_type} - {self.user_id}"
