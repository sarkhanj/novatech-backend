from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from novatech.models import Dataset, Regions, Records
from novatech.serializers import DatasetSerializer, RegionsSerializer, RecordsSerializer

from django.core.files.storage import default_storage
from novatech.ml import train, predict_




@csrf_exempt
def datasetApi(request, id=0):
    if request.method == 'GET':
        dataset = Dataset.objects.all()
        dataset_serializer = DatasetSerializer(dataset, many=True)
        return JsonResponse(dataset_serializer.data, safe=False)


def regionsApi(request, id=0):
    train()
    if request.method == 'GET':
        regions = Regions.objects.all()
        regions_serializer = RegionsSerializer(regions, many=True)
        return JsonResponse(regions_serializer.data, safe=False)



# Only selected ID region records here
def recordsApi(request, id=0):
    if request.method == 'GET':
        records = Records.objects.filter(region_id = id)
        # records = Records.objects.all()
        records_serializer = RecordsSerializer(records, many=True)
        return JsonResponse(records_serializer.data, safe=False)


def mlApi(request, id=0):
    if request.method == 'GET':
        record = Records.objects.filter(id = id)
        # print(record[0])
        result =predict_(record[0])
        # result_serializer = RecordsSerializer(record, many=True)
        # return JsonResponse(records_serializer.data, safe=False)
        return JsonResponse(result,safe=False)
    