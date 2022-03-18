# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer


class SensorView(CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView):
    """Класс для сенсоров"""
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    # def create_sensor(self, request, *args):
    #     self.post(request, *args)
    #     return Response({'status': 'Датчик добавлен'})
    #
    # def update_sensor(self, request, *args):
    #     self.post(request, *args)
    #     return Response({'status': 'Датчик обновлен'})


class MeasurementsView(CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView):
    """Класс для измерений"""

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    # def add_measurment(self, request, *args):
    #     self.post(request, *args)
    #     return Response({'status': 'Измерение добавлено'})
