from django.db import models
from django.core.validators import RegexValidator

VEHICLE_TYPES = (
    ("Two", "Two Wheelers"),
    ("Three", "Three Wheelers"),
    ("Four", "Four Wheelers"),
)

class VehicleModel(models.Model):
    vehicle_number = models.CharField(
        max_length=14,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}[0-9]{2}[A-Z]{1,3}[0-9]{1,4}$',
                message='Enter a valid Indian vehicle number'
            )
        ]
    )
    vehicle_type = models.CharField(max_length=5, choices=VEHICLE_TYPES)
    vehicle_model = models.CharField(max_length=50)
    vehicle_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.vehicle_number} - {self.vehicle_model}"
