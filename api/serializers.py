from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Hospbeds


class Hospbedserializer(GeoFeatureModelSerializer):
    updation_date_time = serializers.DateTimeField(format="%d-%m-%Y - %H:%M:%S", input_formats=None, default_timezone=None)
    class Meta:
        model = Hospbeds
        geo_field = "geom"
        fields = "__all__"
