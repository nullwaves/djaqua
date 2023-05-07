from django.db import models
from django.urls import reverse
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

    name = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255)
    volume = models.IntegerField()
    tank_type = models.CharField(
        max_length=2,
        choices=TANK_TYPE_CHOICES,
        default=FRESHWATER,
    )
    substrate = models.CharField(max_length=255)
    filter_media = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('tank_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Inhabitant(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('fish_detail', kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class WaterTest(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    date_tested = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2) 
    ammonia_level = models.DecimalField(max_digits=5, decimal_places=4)
    nitrite_level = models.DecimalField(max_digits=5, decimal_places=4)
    nitrate_level = models.DecimalField(max_digits=5, decimal_places=2)
    ph_level = models.DecimalField(max_digits=5, decimal_places=2)
    salinity = models.DecimalField(max_digits=5, decimal_places=2)
    notes = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('watertest_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return f"{self.tank.name} - {self.date_tested}"

class Spawn(models.Model):
    spawn_date = models.DateField()
    breeders = models.ManyToManyField(Inhabitant, related_name='spawns_produced')
    hatch_date = models.DateField(blank=True, null=True)
    fry_quantity = models.IntegerField(blank=True, null=True)
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    water_test = models.ForeignKey(WaterTest, on_delete=models.SET_NULL, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        breeders = ', '.join(str(breeder.name) for breeder in self.breeders.all())
        return f"{breeders} - {self.spawn_date}"
