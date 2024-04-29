from django.db import models

from ticket_selling_app.models.common_models import City


class Airport(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Plane(models.Model):
    plane_number = models.CharField(max_length=100)


class PlaneTravel(models.Model):
    plane_id = models.ForeignKey(Plane, on_delete=models.CASCADE)
    airport_departure_id = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="airport_departure"
    )
    airport_arrival_id = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="airport_arrival"
    )
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()


class PlaneTicket(models.Model):
    plane_travel_id = models.ForeignKey(PlaneTravel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
