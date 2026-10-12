from django.db import models

# Create your models here.

class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CONFIRMED = "confirmed", "Confirmed"
        REJECTED = "rejected", "Rejected"
        CANCELLED = "cancelled", "Cancelled"

    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    reference_no = models.CharField(
        max_length=50,
        unique=True,
    )
    request_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    confirmed_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    cancelled_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        db_table = "bookings"

    def __str__(self):
        return f"{self.reference_no} - {self.status}"
        
        
class Payment(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    booking = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE,
        related_name="payments",
    )
    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="payments",
    )
    rental_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    service_fee = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )
    payment_reference = models.CharField(
        max_length=100,
        unique=True,
    )
    payment_method = models.CharField(
        max_length=50,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )
    paid_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    class Meta:
        db_table = "payments"

    def __str__(self):
        return f"{self.payment_reference} - {self.status}"
        
        
        
class Receipt(models.Model):
    payment = models.ForeignKey(
        Payment,
        on_delete=models.CASCADE,
        related_name="receipts",
    )
    receipt_number = models.CharField(
        max_length=50,
        unique=True,
    )
    issued_at = models.DateTimeField()

    class Meta:
        db_table = "receipts"

    def __str__(self):
        return self.receipt_number
