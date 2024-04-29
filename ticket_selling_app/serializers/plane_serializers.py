from rest_framework import serializers

from ticket_selling_app.models.plane_models import (
    Airport,
    Plane,
    PlaneTicket,
    PlaneTravel,
)


class AirportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = "__all__"


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = "__all__"


class PlaneTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaneTravel
        fields = "__all__"


class PlaneTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaneTicket
        fields = "__all__"
