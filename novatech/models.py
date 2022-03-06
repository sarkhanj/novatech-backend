from django.db import models

# Create your models here.
class Dataset(models.Model):
    N = models.IntegerField()
    P = models.IntegerField()
    K = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    label = models.CharField(max_length=50)


class Regions(models.Model):
    region_id = models.AutoField(primary_key=True, null=False)
    region = models.CharField(max_length=50)


class Records(models.Model):
    N = models.IntegerField()
    P = models.IntegerField()
    K = models.IntegerField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    ph = models.FloatField()
    rainfall = models.FloatField()
    region_id = models.ForeignKey(Regions,on_delete = models.CASCADE)

