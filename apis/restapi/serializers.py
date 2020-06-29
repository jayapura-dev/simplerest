from rest_framework import serializers
from ..models import Distrik, Kampung

class DistrikSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Distrik
        fields = ('id_distrik','nama_distrik')


class KampungSerializers(serializers.ModelSerializer):

    class Meta:
        model = Kampung
        fields = ('id_kampung','distrik','nama_kampung')