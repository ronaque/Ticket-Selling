from rest_framework import serializers

from ticket_selling_app.models.bus_models import Bus, BusStation, BusTicket, BusTravel


class BusStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStation
        fields = "__all__"


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = "__all__"


class BusTravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTravel
        fields = "__all__"


class BusTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusTicket
        fields = "__all__"
