from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Tank, Inhabitant, WaterTest, Spawn

class TankModelTest(TestCase):
    def setUp(self):
        self.tank = Tank.objects.create(
            name="Tank 1",
            location="Living room",
            volume=50,
            tank_type=Tank.FRESHWATER,
            substrate="Sand",
            filter_media="Sponge filter",
            notes="Test notes",
        )

    def test_tank_str(self):
        self.assertEqual(str(self.tank), "Tank 1")

    def test_tank_absolute_url(self):
        url = reverse("tank_detail", kwargs={"pk": self.tank.pk})
        self.assertEqual(self.tank.get_absolute_url(), url)

    def test_tank_name_unique(self):
        with self.assertRaises(Exception):
            tank2 = Tank.objects.create(
                name="Tank 1",
                location="Bedroom",
                volume=20,
                tank_type=Tank.SALTWATER,
                substrate="Gravel",
                filter_media="Canister filter",
                notes="Another test notes",
            )


class InhabitantModelTest(TestCase):
    def setUp(self):
        self.tank = Tank.objects.create(
            name="Tank 1",
            location="Living room",
            volume=50,
            tank_type=Tank.FRESHWATER,
            substrate="Sand",
            filter_media="Sponge filter",
            notes="Test notes",
        )

        self.inhabitant = Inhabitant.objects.create(
            name="Fish 1",
            species="Guppy",
            quantity=5,
            tank=self.tank,
            notes="Test notes",
        )

    def test_inhabitant_str(self):
        self.assertEqual(str(self.inhabitant), "Fish 1")

    def test_inhabitant_quantity_positive(self):
        with self.assertRaises(Exception):
            inhabitant2 = Inhabitant.objects.create(
                name="Fish 2",
                species="Neon tetra",
                quantity=-2,
                tank=self.tank,
                notes="Test notes",
            )


class WaterTestModelTest(TestCase):
    def setUp(self):
        self.tank = Tank.objects.create(
            name="Tank 1",
            location="Living room",
            volume=50,
            tank_type=Tank.FRESHWATER,
            substrate="Sand",
            filter_media="Sponge filter",
            notes="Test notes",
        )

        self.water_test = WaterTest.objects.create(
            tank=self.tank,
            date_tested="2022-01-01",
            temperature=25.5,
            ammonia_level=0.25,
            nitrite_level=0.1,
            nitrate_level=10.0,
            ph_level=7.5,
            salinity=0.0,
            notes="Test notes",
        )

    def test_water_test_str(self):
        self.assertEqual(
            str(self.water_test), "Tank 1 - 2022-01-01"
        )


class SpawnModelTestCase(TestCase):
    def setUp(self):
        self.tank = Tank.objects.create(
            name='Tank A', 
            location='Living Room',
            volume=10, 
            substrate='Sand', 
            filter_media='Sponge', 
            tank_type='FW'
            )
        self.test_date = timezone.now().date()
        self.water_test = WaterTest.objects.create(
            tank=self.tank, 
            date_tested=self.test_date, 
            temperature=25.5, 
            ammonia_level=0.25, 
            nitrite_level=0.1, 
            nitrate_level=20, 
            ph_level=7.2, 
            salinity=0.0
            )
        self.breeder1 = Inhabitant.objects.create(
            name='Fish 1', 
            species='Guppy', 
            quantity=2, 
            tank=self.tank
            )
        self.breeder2 = Inhabitant.objects.create(
            name='Fish 2', 
            species='Guppy', 
            quantity=1, 
            tank=self.tank
            )

    def test_create_spawn(self):
        spawn = Spawn.objects.create(
            spawn_date=self.test_date, 
            tank=self.tank, 
            hatch_date=self.test_date + timezone.timedelta(days=7), 
            fry_quantity=10, 
            water_test=self.water_test, 
            notes='Test notes'
            )
        self.assertEqual(Spawn.objects.count(), 1)

    def test_create_spawn_with_breeders(self):
        spawn = Spawn.objects.create(spawn_date=self.test_date, tank=self.tank, hatch_date=self.test_date + timezone.timedelta(days=7), fry_quantity=10, water_test=self.water_test, notes='Test notes')
        spawn.breeders.add(self.breeder1, self.breeder2)
        self.assertEqual(spawn.breeders.count(), 2)

    def test_spawn_string_representation(self):
        spawn = Spawn.objects.create(spawn_date=self.test_date, tank=self.tank, hatch_date=self.test_date + timezone.timedelta(days=7), fry_quantity=10, water_test=self.water_test, notes='Test notes')
        spawn.breeders.add(self.breeder1, self.breeder2)
        self.assertEqual(str(spawn), f'{self.breeder1.name}, {self.breeder2.name} - {self.test_date}')