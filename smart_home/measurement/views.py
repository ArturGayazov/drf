# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorMeasurmentSerializer


class SensorViewCU(CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView):
    """Класс для сенсоров"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsViewCU(CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView):
    """Класс для измерений"""

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorMeasurementView(CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView):
    """Класс для отображения всех данных"""

    queryset = Sensor.objects.all()
    serializer_class = SensorMeasurmentSerializer

