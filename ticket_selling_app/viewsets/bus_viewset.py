from rest_framework import viewsets

from ticket_selling_app.models.bus_models import Bus
from ticket_selling_app.serializers.bus_serializers import BusSerializer


class BusViewSet(viewsets.ModelViewSet):
    queryset = Bus.objects.all()
    serializer_class = BusSerializer