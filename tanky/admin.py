from django.contrib import admin
from .models import Tank, Inhabitant, WaterTest, Spawn

@admin.register(Tank)
class TankAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'volume', 'tank_type')
    list_filter = ('tank_type',)
    search_fields = ('name', 'location', 'tank_type')
    ordering = ('name',)

@admin.register(Inhabitant)
class InhabitantAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'quantity', 'tank')
    list_filter = ('tank',)
    search_fields = ('name', 'species', 'tank__name')
    ordering = ('name',)

@admin.register(WaterTest)
class WaterTestAdmin(admin.ModelAdmin):
    list_display = ('tank', 'date_tested', 'temperature', 'ammonia_level', 'nitrite_level', 'nitrate_level', 'ph_level', 'salinity')
    list_filter = ('tank',)
    search_fields = ('tank__name',)
    ordering = ('-date_tested',)

@admin.register(Spawn)
class SpawnAdmin(admin.ModelAdmin):
    list_display = ('spawn_date', 'breeders_list', 'hatch_date', 'fry_quantity', 'tank', 'water_test')
    list_filter = ('tank', 'breeders')
    search_fields = ('breeders__name', 'tank__name')
    ordering = ('-spawn_date',)

    def breeders_list(self, obj):
        return ', '.join([i.name for i in obj.breeders.all()])
    breeders_list.short_description = 'Breeders'
