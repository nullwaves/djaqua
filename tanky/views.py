from django.views.generic.base import TemplateView
from django.shortcuts import render

# Create your views here.
class IndexView(TemplateView):
    template_name = 'tanky/base.html'
