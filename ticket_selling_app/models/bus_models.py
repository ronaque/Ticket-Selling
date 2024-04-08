from django.db import models

from ticket_selling_app.models.common_models import City


class BusStation(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Bus(models.Model):
    bus_number = models.CharField(max_length=100)

class BusTravel(models.Model):
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    bus_station_departure_id = models.ForeignKey(BusStation, on_delete=models.CASCADE, related_name='bus_station_departure')
    bus_station_arrival_id = models.ForeignKey(BusStation, on_delete=models.CASCADE, related_name='bus_station_arrival')
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

class BusTicket(models.Model):
    bus_travel_id = models.ForeignKey(BusTravel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)