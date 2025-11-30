from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

ROLE_CHOICES = (
    ("superadmin", "superadmin"),
    ("admin", "admin"),
    ("user", "user"),
)

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")
    created_at = models.DateTimeField(auto_now_add=True)   



