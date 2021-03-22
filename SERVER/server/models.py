from django.db import models
from django.utils import timezone

# Create your models here.

class Weather(models.Model):
    hora = models.DateTimeField(default=timezone.now)
    temperatura = models.TextField()
    umidade = models.TextField()
    luminosidade = models.TextField()