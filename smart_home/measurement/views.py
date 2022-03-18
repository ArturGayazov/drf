# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorViewCU(CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView):
    """Класс для сенсоров"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsViewCU(CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView):
    """Класс для измерений"""

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

