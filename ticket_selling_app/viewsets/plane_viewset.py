from rest_framework import viewsets

from ticket_selling_app.models.plane_models import Plane
from ticket_selling_app.serializers.plane_serializers import PlaneSerializer


class PlaneViewSet(viewsets.ModelViewSet):
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer