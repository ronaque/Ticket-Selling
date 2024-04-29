from rest_framework import serializers

from ticket_selling_app.models.common_models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"
