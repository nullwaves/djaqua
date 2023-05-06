from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Inhabitant, Tank, Spawn, WaterTest

# Create your views here.
class IndexView(TemplateView):
    template_name = 'tanky/base.html'

class TankListView(ListView):
    model = Tank

class TankCreateView(CreateView):
    model = Tank
    fields = ['name', 'location', 'volume', 'tank_type', 'substrate', 'filter_media', 'notes']

class TankEditView(UpdateView):
    model = Tank
    fields = ['location', 'tank_type', 'substrate', 'filter_media', 'notes']

class TankDetailView(DetailView):
    model = Tank

class InhabitantCreateView(CreateView):
    model = Inhabitant
    fields = ['name', 'species', 'quantity', 'notes']

class WaterTestCreateView(CreateView):
    model = WaterTest
    fields = ['date_tested', 'temperature', 'ph_level', 'ammonia_level', 'nitrite_level', 'nitrate_level', 'salinity', 'notes']

class SpawnCreateView(CreateView):
    model = Spawn
    fields = ['spawn_date', 'breeders', 'hatch_date', 'fry_quantity', 'water_test', 'notes']