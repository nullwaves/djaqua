"""
URL configuration for djaqua project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tanky import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tanks/', views.TankListView.as_view(), name='tank_list'),
    path('tank/new', views.TankCreateView.as_view(), name='tank_create'),
    path('tank/<int:pk>/', views.TankDetailView.as_view(), name='tank_detail'),
    path('tank/<int:pk>/new', views.InhabitantCreateView.as_view(), name='fish_create'),
    path('tank/<int:pk>/test', views.WaterTestCreateView.as_view(), name='watertest_create'),
    path('tank/<int:pk>/edit', views.TankEditView.as_view(), name='tank_edit'),
    path('test/<int:pk>/', views.WaterTestDetailView.as_view(), name='watertest_detail'),
    path('fish/<int:pk>/', views.InhabitantDetailView.as_view(), name='fish_detail'),
    path('fish/<int:pk>/edit', views.InhabitantEditView.as_view(), name='fish_edit'),
    path('admin/', admin.site.urls),
]
