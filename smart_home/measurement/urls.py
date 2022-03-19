from django.urls import path
from .views import *
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateListView.as_view()),
    path('sensors/<pk>/', SensorDetailUpdateView.as_view()),
    path('measurements/', AddMeasurementView.as_view()),
]


