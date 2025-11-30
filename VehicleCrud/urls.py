from django.urls import path
from .views import VehicleView

urlpatterns = [
    path('vehicles/', VehicleView.as_view(), name='vehicles'),
    path('vehicles/<int:vehicle_id>/', VehicleView.as_view(), name='vehicle-detail'),
]
