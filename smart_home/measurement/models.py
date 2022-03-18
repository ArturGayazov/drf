from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)


class Measurement(models.Model):
    sensor = models.IntegerField()
    temperature = models.FloatField()
    created_at = models.DateField(auto_now=True)
    update_at = models.DateField(auto_now_add=True)

