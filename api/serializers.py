from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Hospbeds


class Hospbedserializer(GeoFeatureModelSerializer):
    class Meta:
        model = Hospbeds
        geo_field = "geom"
        fields = "__all__"
