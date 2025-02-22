from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=42, unique=True)