from django.db import models
from simple_history.models import HistoricalRecords

class Tank(models.Model):
    FRESHWATER = 'FW'
    BRACKISH = 'BW'
    SALTWATER = 'SW'
    TANK_TYPE_CHOICES = [
        (FRESHWATER, 'Freshwater'),
        (BRACKISH, 'Brackish'),
        (SALTWATER, 'Saltwater'),
    ]

    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    volume = models.IntegerField()
    tank_type = models.CharField(
        max_length=2,
        choices=TANK_TYPE_CHOICES,
        default=FRESHWATER,
    )
    substrate = models.CharField(max_length=255)
    filter_media = models.CharField(max_length=255)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Inhabitant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    notes = models.TextField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class WaterTest(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2) 
    ammonia_level = models.DecimalField(max_digits=5, decimal_places=4)
    nitrite_level = models.DecimalField(max_digits=5, decimal_places=4)
    nitrate_level = models.DecimalField(max_digits=5, decimal_places=2)
    ph_level = models.DecimalField(max_digits=5, decimal_places=2)
    salinity = models.DecimalField(max_digits=5, decimal_places=2)
    date_tested = models.DateField()

    def __str__(self):
        return f"{self.tank.name} - {self.date_tested}"
