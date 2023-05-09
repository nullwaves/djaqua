from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

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
    fields = ['name', 'location', 'tank_type', 'substrate', 'filter_media', 'notes']

class TankDetailView(DetailView):
    model = Tank

class InhabitantCreateView(CreateView):
    model = Inhabitant
    fields = ['name', 'species', 'quantity', 'notes']

    def form_valid(self, form):
        form.instance.tank = get_object_or_404(Tank, pk=self.kwargs['pk'])
        return super().form_valid(form)

class InhabitantEditView(UpdateView):
    model = Inhabitant
    fields = ['name', 'species', 'tank', 'quantity', 'notes']

class InhabitantDetailView(DetailView):
    model = Inhabitant

class WaterTestCreateView(CreateView):
    model = WaterTest
    fields = ['date_tested', 'temperature', 'ph_level', 'ammonia_level', 'nitrite_level', 'nitrate_level', 'salinity', 'notes']
    
    def form_valid(self, form):
        form.instance.tank = get_object_or_404(Tank, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
class WaterTestDetailView(DetailView):
    model = WaterTest

class SpawnCreateView(CreateView):
    model = Spawn
    fields = ['spawn_date', 'breeders', 'hatch_date', 'fry_quantity', 'water_test', 'notes']