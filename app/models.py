from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.

class Form(models.Model):
    
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    event_date = models.DateField(null=True)
    
    def __str__(self):
        return self.name
    