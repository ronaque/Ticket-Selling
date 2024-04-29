from rest_framework import viewsets

from ticket_selling_app.models.plane_models import PlaneTravel
from ticket_selling_app.serializers.plane_serializers import PlaneTravelSerializer


class PlaneTravelViewSet(viewsets.ModelViewSet):
    queryset = PlaneTravel.objects.all()
    serializer_class = PlaneTravelSerializer
