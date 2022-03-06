from novatech.models import Dataset, Regions, Records
from rest_framework import serializers

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dataset
        fields = ('N','P','K','temperature','humidity','ph','rainfall','label')


class RegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regions
        fields = ('region_id','region')


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ('N', 'P', 'K', 'temperature',
                  'humidity', 'ph', 'rainfall', 'region_id')

